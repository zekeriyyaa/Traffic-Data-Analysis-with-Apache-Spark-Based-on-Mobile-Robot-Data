import MsSQLConnectorClass as MsSQL
import numpy as np
import datetime


### Match packages and ways if they are at the same coordinates.
def GetSelected(packets):
    ### get MsSQL connection
    MsSQLConnector1 = MsSQL.MsSQLConnection()
    MsSQLConnector2 = MsSQL.MsSQLConnection()
    MsSQLConnector3 = MsSQL.MsSQLConnection()

    conn1 = MsSQLConnector1.GetConnection()
    conn2 = MsSQLConnector2.GetConnection()
    conn3 = MsSQLConnector3.GetConnection()

    cursor1 = conn1.cursor()
    cursor2 = conn2.cursor()
    cursor3 = conn3.cursor()

    ### get way's information from MsSQL
    cursor1.execute("SELECT Way_ID,Way_SpeedLimit,Way_LineWidth,Way_Length FROM DefWays")

    ### get robot's information from MsSQL
    cursor3.execute("SELECT Rbt_ID,Rbt_Length FROM DefRobots")
    robot_length_list={}
    for rbt in cursor3:
        robot_length_list[str(rbt[0])]=rbt[1]
    selected=[]

    # initialize stop speed value
    stopSpeed=0.001

    # look all way to which packet meet it
    for way in cursor1:
        # assign specific way ID
        wayID = str(way[0])
        # get half way width
        half_WayWidth = way[2] / 2
        # get way length
        WayLength = float(way[3])

        ## get way coordinate information from MsSQL
        cursor2.execute("SELECT n.Nd_Latitute, n.Nd_Longtitute from DefWays w INNER JOIN  DefWaypoints wp ON wp.Wyp_WayID = w.Way_ID INNER JOIN DefNodes n ON n.Nd_ID = wp.Wyp_NodeID Where w.Way_ID = " + wayID + " AND wp.Wyp_EnterExitCode IN ('0','1')")

        coordinates = []
        ## get ways to list
        for row in cursor2:
            ## tek bır yol ıcın kullanılacak dıct. hazırlanıyor
            coordinate = {"latitute": "", "longtitute": ""}
            coordinate["latitute"] = row[0]
            coordinate["longtitute"] = row[1]
            ## ways added list
            coordinates.append(coordinate)

        ## call a function that find a corner of ways with given ways information
        linesCoordinates = CalculateRectLineCoordinate(coordinates, half_WayWidth, WayLength)

        ## check the way coordinate and compare them with packet's coordinate, and deside whether packer created at the same way
        select = CheckCoordinate(linesCoordinates, packets, wayID,WayLength,stopSpeed,robot_length_list);

        # if packet created on the current way, add it "select" list
        selected.extend(select)
    return selected

# A utility function to calculate
# area of triangle formed by (x1, y1),
# (x2, y2) and (x3, y3)
def area(x1, y1, x2, y2, x3, y3):
    return abs((x1 * (y2 - y3) +x2 * (y3 - y1) +x3 * (y1 - y2)) / 2.0)

# A function to check whether point
# P(x, y) lies inside the rectangle
# formed by A(x1, y1), B(x2, y2),
# C(x3, y3) and D(x4, y4)
def checkC(x1, y1, x2, y2, x3,y3, x4, y4, x, y):
    # Calculate area of rectangle ABCD
    A = (area(x1, y1, x2, y2, x3, y3) +
         area(x1, y1, x4, y4, x3, y3))

    # Calculate area of triangle PAB
    A1 = area(x, y, x1, y1, x2, y2)

    # Calculate area of triangle PBC
    A2 = area(x, y, x2, y2, x3, y3)

    # Calculate area of triangle PCD
    A3 = area(x, y, x3, y3, x4, y4)

    # Calculate area of triangle PAD
    A4 = area(x, y, x1, y1, x4, y4);

    # Check if sum of A1, A2, A3
    # and A4 is same as A

    return (round(A,7) == round(A1 + A2 + A3 + A4,7))

### check the given packets coordinate and find which is in the current way
def CheckCoordinate(list, packets, wayID,WayLength,stopSpeed,robot_length_list):

    selected = []

    wayCount = 0;
    wayCountCheck = -1;

    for packet in packets:
        # use for add tourCount
        temp = []
        for t in packet:
            temp.append(t)

        # check: default true. if packet is on the current way value is true else false.
        check = True

        # check coordinate whether packet is on the current way with given way coordinates and packet
        if (not checkC(list[0],list[1],list[2],list[3],list[4],list[5],list[6],list[7],packet[1],packet[2])):
            #plt.scatter(x=packet[1], y=packet[2], color="red")
            check = False
            wayCountCheck = -1
        if (check):
            #plt.scatter(x=packet[1], y=packet[2], color="green")
            if (wayCountCheck != 1):
                wayCount += 1
            temp.append(wayCount)
            temp.append(wayID)
            temp.append(WayLength)
            temp.append(robot_length_list[str(temp[5])])

            # check the robot is stopped or moving with given stopSpeed. default 0.001
            # 1 : stop  0 : moving

            if(abs(temp[3])<stopSpeed and abs(temp[4])<stopSpeed):
                temp.append(1)
            else:
                temp.append(0)
            selected.append(temp)
            wayCountCheck = 1

    #plt.show()
    #print("toplam yol üzerinde : ",len(selected),"  yol üzerinde değil",(len(packets)-len(selected)))

    return selected

### find the way cornet points' coordinates with given way coordinate, way width and length
def CalculateRectLineCoordinate(coordinats, half_WayWidth, wayLenght):
    ## coordınatları tutacak listesi tanımlanıyor.
    Coordinatelist = []

    # sinus değerlerni hesaplama ~ başlangıç

    # yolun y2 - y1 farkı sinüs için
    dify2y1 = abs(coordinats[1]["longtitute"] - coordinats[0]["longtitute"]);

    # yolun x2 - x1 farkı sinüs için
    difx2x1 = abs(coordinats[1]["latitute"] - coordinats[0]["latitute"]);

    # yolun uzunluğu hesaplanıyor
    # wayLenght = pow(dify2y1,2) + pow(difx2x1,2)
    # wayLenght = pow(wayLenght,0.5)

    # sinüs tetha ve sin alpha hesaplanıyor
    sintetha = dify2y1 / wayLenght;
    sinalpha = difx2x1 / wayLenght;

    # sinus değerlerni hesaplama ~ son

    # yolun genişliğinin yarısının yatay uzunluğu
    xofsquare = sintetha * half_WayWidth;

    # yolun genişliğinin yarısının dikey uzunluğu
    yofsquare = sinalpha * half_WayWidth;

    # Yolun durumunu kontrol ediyor
    # pozitif eğimli mi yoksa neğatif eğimli mi kontrolu
    # eğer positif eğimli ise if in içine girer

    if ((coordinats[0]["latitute"] > coordinats[1]["latitute"] and coordinats[0]["longtitute"] > coordinats[1][
        "longtitute"]) or coordinats[0]["latitute"] < coordinats[1]["latitute"] and coordinats[0]["longtitute"] <
            coordinats[1]["longtitute"]):
        # yolun noktalarını ayarlamak için kullanılıyor
        # şekil : https://drive.google.com/open?id=1ISh5PhXmOlso1T22xzeXJUfWYIH_xVE4
        # şekildeki gibi hesaplamalarımızı yolun genişliğini kullanarak buluyoruz bu nedenle nodeların konumunu şekildeki gibi olması gerekir.
        if (coordinats[0]["latitute"] > coordinats[1]["latitute"] and coordinats[0]["longtitute"] > coordinats[1][
            "longtitute"]):
            tmp = coordinats[0];
            coordinats[0] = coordinats[1];
            coordinats[1] = tmp;

        # sekil : https://drive.google.com/open?id=1ISh5PhXmOlso1T22xzeXJUfWYIH_xVE4
        # şekilde belirtilen nokların hesaplanması ~ begin
        coordinat1lt = {"latitute": "", "longtitute": ""}
        coordinat1lt["longtitute"] = coordinats[1]["longtitute"] - yofsquare;
        coordinat1lt["latitute"] = coordinats[1]["latitute"] + xofsquare;

        coordinat1gt = {"latitute": "", "longtitute": ""}
        coordinat1gt["longtitute"] = coordinats[1]["longtitute"] + yofsquare;
        coordinat1gt["latitute"] = coordinats[1]["latitute"] - xofsquare;

        coordinat0lt = {"latitute": "", "longtitute": ""}
        coordinat0lt["longtitute"] = coordinats[0]["longtitute"] - yofsquare;
        coordinat0lt["latitute"] = coordinats[0]["latitute"] + xofsquare;

        coordinat0gt = {"latitute": "", "longtitute": ""}
        coordinat0gt["longtitute"] = coordinats[0]["longtitute"] + yofsquare;
        coordinat0gt["latitute"] = coordinats[0]["latitute"] - xofsquare;
        # şekilde belirtilen nokların hesaplanması ~ end

        # yolun 4 köşesinin koordinatları listeye eklendi.
        Coordinatelist.append(coordinat0lt["latitute"]);
        Coordinatelist.append(coordinat0lt["longtitute"]);
        Coordinatelist.append(coordinat1lt["latitute"]);
        Coordinatelist.append(coordinat1lt["longtitute"]);
        Coordinatelist.append(coordinat1gt["latitute"]);
        Coordinatelist.append(coordinat1gt["longtitute"]);
        Coordinatelist.append(coordinat0gt["latitute"]);
        Coordinatelist.append(coordinat0gt["longtitute"]);

    # pozitif eğimli mi yoksa neğatif eğimli mi kontrolu
    # eğer negatif eğimli ise else in içine girer

    else:
        # yolun noktalarını ayarlamak için kullanılıyor
        # şekil : https://drive.google.com/open?id=1qoiPwURDgAL8j8Uh8Rsz89B-iLqigf6s
        # şekildeki gibi hesaplamalarımızı yolun genişliğini kullanarak buluyoruz bu nedenle nodeların konumunu şekildeki gibi olması gerekir.
        if (coordinats[0]["latitute"] < coordinats[1]["latitute"] and coordinats[0]["longtitute"] > coordinats[1][
            "longtitute"]):
            tmp = coordinats[0];
            coordinats[0] = coordinats[1];
            coordinats[1] = tmp;

        # sekil : https://drive.google.com/open?id=1qoiPwURDgAL8j8Uh8Rsz89B-iLqigf6s
        # şekilde belirtilen nokların hesaplanması ~ begin
        coordinat1lt = {"latitute": "", "longtitute": ""}
        coordinat1lt["longtitute"] = coordinats[1]["longtitute"] - yofsquare;
        coordinat1lt["latitute"] = coordinats[1]["latitute"] - xofsquare;

        coordinat1gt = {"latitute": "", "longtitute": ""}
        coordinat1gt["longtitute"] = coordinats[1]["longtitute"] + yofsquare;
        coordinat1gt["latitute"] = coordinats[1]["latitute"] + xofsquare;

        coordinat0lt = {"latitute": "", "longtitute": ""}
        coordinat0lt["longtitute"] = coordinats[0]["longtitute"] - yofsquare;
        coordinat0lt["latitute"] = coordinats[0]["latitute"] - xofsquare;

        coordinat0gt = {"latitute": "", "longtitute": ""}
        coordinat0gt["longtitute"] = coordinats[0]["longtitute"] + yofsquare;
        coordinat0gt["latitute"] = coordinats[0]["latitute"] + xofsquare;
        # şekilde belirtilen nokların hesaplanması ~ end

        # yolun 4 köşesinin koordinatları listeye eklendi.
        Coordinatelist.append(coordinat0lt["latitute"]);
        Coordinatelist.append(coordinat0lt["longtitute"]);
        Coordinatelist.append(coordinat1lt["latitute"]);
        Coordinatelist.append(coordinat1lt["longtitute"]);
        Coordinatelist.append(coordinat1gt["latitute"]);
        Coordinatelist.append(coordinat1gt["longtitute"]);
        Coordinatelist.append(coordinat0gt["latitute"]);
        Coordinatelist.append(coordinat0gt["longtitute"]);

    return Coordinatelist
