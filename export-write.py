import exportRead
import os
import shutil
import time
originalFile = "export/scripts/G01P01B.xml"
to = ""

def getWrited(original,to):
    version = "0.0.0.2"
    subdir = to + original.split("/")[len(original.split("/"))-1]
    try:
        shutil.rmtree(subdir)
    except:
        pass
    inc = 0
    end = False
    while (not end) and inc < 100:
        try:
            os.mkdir(subdir)
            end = True
        except:
            time.sleep(1)
    
    data = exportRead.getData(original)
    print("writing LSDTable")
    LSD = ""
    for loop in data["LSDTable"]:
        LSD = LSD + loop + "\n"
    temp = open(subdir + "/LSD.txt","w")
    temp.write(LSD)
    temp.close()
    INI = ""
    INI = INI + "game = " + data["game"]["version"]+"\n"
    INI = INI + "region = " + data["game"]["region"]
    temp = open(subdir + "/info.ini","w")
    temp.write(INI)
    temp.close()

    script = data["script"]
    for loop in script:
        pname = loop["name"]
        os.mkdir(subdir + "/" + pname)
        nsub = subdir + "/" + pname
        print(nsub)
        temp = open(nsub + "/script.pms", "w")
        temp.write(toCode(loop))
        temp.close()

def toCode(fonction):
    rendu = ""
    deb = "    "
    for fonc in fonction["fonction"]:
        rendu = rendu + fonc["id"] + ":\n"
        for comm in fonc["funcl"]:
            commande = comm["commande"]
            if commande == "end":
                rendu = rendu + deb + "#end\n"
            elif commande == "wait":
                rendu = rendu + deb + "wait " + comm["duration"] + "\n"
            elif commande == "back2SetMode":
                rendu = rendu + deb + "back2SetMode " + comm["param"] + "\n"
            elif commande == "screenFadeOut":
                if comm["bool"] == "1":
                    boole = "True"
                else:
                    boole = "False"
                rendu = rendu + deb + "screenFadeOut duration = " + comm["duration"] + ", bool = " + boole + "\n"
            elif commande == "screen2FadeOut":
                if comm["bool"] == "1":
                    boole = "True"
                else:
                    boole = "False"
                rendu = rendu + deb + "screen2FadeOut duration = " + comm["duration"] + ", bool = " + boole + "\n"
            elif commande == "lives":
                rendu = rendu + deb + "lives " + comm["actorid"] + ":\n"
                rendu = rendu + deb + deb + "TODO\n"
            elif commande == "messageClose":
                rendu = rendu + deb + "messageClose\n"
            elif commande == "messageSwitchTalk":
                rendu = rendu + deb + "messageSwitchTalk " + comm["svar"] + ":\n"
                for loop in comm["case"]:
                    if loop["type"]=="int":
                        rendu = rendu + deb + deb + "case " + loop["value"] + ":\n"
                        for loop2 in loop["text"]:
                            rendu = rendu + deb + deb + deb + loop2[0] + " = '" + loop2[1] + "'\n"
                    else:
                        print("erreur : type non spécifié")
                rendu = rendu + deb + deb + "default:\n"
                for loop in comm["default"]:
                    rendu = rendu + deb + deb + deb + loop[0] + " = '" + loop[1] + "'\n"
            elif commande == "switchSector":
                rendu = rendu + deb + "switchSector:\n"
                rendu = rendu + deb + deb + "TODO\n"
            elif commande == "screenFadeOutAll":
                if comm["bool"] == "1":
                    boole = "True"
                else:
                    boole = "False"
                rendu = rendu + deb + "screenFadeOutAll duration = " + comm["duration"] + ", bool = " + boole +"\n"
            elif commande == "backSetGround":
                rendu = rendu + deb + "backSetGround " + comm["levelid"] + "\n"
            elif commande == "label":
                rendu = rendu + deb + "@" + comm["id"] + "\n"
            elif commande == "supervisionStationCommon":
                rendu = rendu + deb + "supervisionStationCommon " + comm["stationid"] + "\n"
            elif commande == "switch":
                rendu = rendu + deb + "switch " + comm["svar"] + "\n"
            elif commande == "jump":
                rendu = rendu + deb + "jump @" + comm["tolabel"] + "\n"
            elif commande == "debugPrint":
                rendu = rendu + deb + "debugPrint " + comm["constref"] + "\n"
            elif commande == "bgmPlayFadeIn":
                rendu = rendu + deb + "bgmPlayFadeIn bgm = " + comm["bgm"] + ", duration = " + comm["duration"] + ", volume = " + comm["vol"] + "\n"
            elif commande == "jumpCommon":
                rendu = rendu + deb + "jumpCommon " + comm["croutineid"] + "\n"
            elif commande == "setAnimation":
                rendu = rendu + deb + "setAnimation " + comm["animid"] + "\n"
            elif commande == "waitScreenFade":
                rendu = rendu + deb + "waitScreenFade\n"
            elif commande == "waitScreenFadeAll":
                rendu = rendu + deb + "waitScreenFadeAll"
            elif commande == "soundStop":
                rendu = rendu + deb + "soundStop\n"
            elif commande == "back2SetGround":
                rendu = rendu + deb + "back2SetGround " + comm["levelid"] + "\n"
            elif commande == "supervisionActing":
                rendu = rendu + deb + "supervisionActing " + comm["layerid"] + "\n"
            elif commande == "performer":
                rendu = rendu + deb + "performer " + comm["performerid"] + ":\n"
                rendu = rendu + deb + deb + "TODO\n"
            elif commande == "screen2FadeIn":
                if comm["bool"] == "1":
                    boole = "True"
                else:
                    boole = "False"
                rendu = rendu + deb + "screen2FadeIn duration = " + comm["duration"] + ", bool = " + boole + "\n"
            elif commande == "screenFadeIn":
                if comm["bool"] == "1":
                    boole = "True"
                else:
                    boole = "False"
                rendu = rendu + deb + "screenFadeIn duration = " + comm["duration"] + ", bool = " + boole + "\n"
            elif commande == "messageSetFace":
                rendu = rendu + deb + "messageSetFace actor = " + comm["actorid"] + ", face = " + comm["face"] + ", facemode = " + comm["facemode"] + "\n"
            elif commande == "callCommon":
                rendu = rendu + deb + "callCommon " + comm["croutineid"] + "\n"
            elif commande == "waitExecuteLives":
                rendu = rendu + deb + "waitExecuteLives " + comm["actorid"] + "\n"
            elif commande == "sePlay":
                rendu = rendu + deb + "sePlay " + comm["param"] + "\n"
            elif commande == "messageResetActor":
                rendu = rendu + deb + "messageResetActor\n"
            elif commande == "messageTalk":
                rendu = rendu + deb + "messageTalk:\n"
                for loop in comm["text"]:
                    rendu = rendu + deb + deb + loop[0] + " = '" + loop[1] + "'\n"
            elif commande == "camera2SetPositionMark":
                rendu = rendu + deb + "camera2SetPositionMark " + comm["param"] + " " + comm["param_1"] + " " + comm["param_2"] + " " + comm["param_3"] + "\n"
            elif commande == "supervisionRemoveActing":
                rendu = rendu + deb + "supervisionRemoveActing " + comm["layerid"] + "\n"
            elif commande == "waitExecutePerformer":
                rendu = rendu + deb + "waitExecutePerformer " + comm["performerid"] + "\n"
            elif commande == "messageSetFaceOnly":
                rendu = rendu + deb + "messageSetFaceOnly actorid = " + comm["actorid"] + ", face = " + comm["face"] + ", " + comm["param_2"] + "\n"
            elif commande == "bgmFadeOut":
                rendu = rendu + deb + "bgmFadeOut " + comm["duration"] + "\n"
            elif commande == "backSetBanner2":
                rendu = rendu + deb + "backSetBanner2 " + comm["param"] + ", " + comm["param_1"] + ", x = " + comm["x"] + ", y = " + comm["y"] + ", " + comm["param_4"] + "\n"
            elif commande == "flagSetScenario":
                rendu = rendu + deb + "flagSetScenario svar = " + comm["svar"] + ", " + comm["param_1"] + ", " + comm["param_2"] + "\n"
            elif commande == "messageSwitchMonologue":
                rendu = rendu + deb + "messageSwitchMonologue " + comm["svar"] + ":\n"
                for loop in comm["case"]:
                    if loop["type"]=="int":
                        rendu = rendu + deb + deb + "case " + loop["value"] + ":\n"
                        for loop2 in loop["text"]:
                            rendu = rendu + deb + deb + deb + loop2[0] + " = '" + loop2[1] + "'\n"
                    else:
                        print("erreur : type non spécifié")
                rendu = rendu + deb + deb + "default:\n"
                for loop in comm["default"]:
                    rendu = rendu + deb + deb + deb + loop[0] + " = '" + loop[1] + "'\n"
            elif commande == "messageSetActor":
                rendu = rendu + deb + "messageSetActor " + comm["actorid"] + "\n"
            elif commande == "cameraSetPositionMark":
                rendu = rendu + deb + "cameraSetPositionMark " + comm["param"] + ", " + comm["param_1"] + ", " + comm["param_2"] + ", " + comm["param_3"] + "\n"
            elif commande == "object":
                rendu = rendu + deb + "object " + comm["objectid"] + ":\n"
                rendu = rendu + deb + deb + "TODO\n"
            elif commande == "cameraSetEffect":
                rendu = rendu + deb + "cameraSetEffect " + comm["param"] + ", " + comm["param_1"] + ", " + comm["param_2"] + "\n"
            elif commande == "waitExecuteObject":
                rendu = rendu + deb + "waitExecuteObject " + comm["objectid"] + "\n"
            elif commande == "screen2FlushOut":
                rendu = rendu + deb + "screen2FlushOut " + comm["param"] + ", " + comm["param_1"] + ", " + comm["param_2"] + ", " + comm["param_3"] + ", " + comm["param_4"] + ", " + comm["param_5"] + "\n"
            elif commande == "screenFlushOut":
                rendu = rendu + deb + "screenFlushOut " + comm["param"] + ", " + comm["param_1"] + ", " + comm["param_2"] + ", " + comm["param_3"] + ", " + comm["param_4"] + ", " + comm["param_5"] + "\n"
            elif commande == "screen2FlushIn":
                rendu = rendu + deb + "screen2FlushIn " + comm["param"] + ", " + comm["param_1"] + ", " + comm["param_2"] + ", " + comm["param_3"] + ", " + comm["param_4"] + ", " + comm["param_5"] + "\n"
            elif commande == "screenFlushIn":
                rendu = rendu + deb + "screenFlushIn " + comm["param"] + ", " + comm["param_1"] + ", " + comm["param_2"] + ", " + comm["param_3"] + ", " + comm["param_4"] + ", " + comm["param_5"] + "\n"
            elif commande == "waitSe":
                rendu = rendu + deb + "waitSe " + comm["param"] + "\n"
            elif commande == "flagSetDungeonMode":
                rendu = rendu + deb + "flagSetDungeonMode " + comm["param"] + ", " + comm["param_1"] + "\n"
            elif commande == "messageEmptyActor":
                rendu = rendu + deb + "messageEmptyActor\n"
            elif commande == "seStop":
                rendu = rendu + deb + "seStop\n"
            elif commande == "waitBgm":
                rendu = rendu + deb + "waitBgm " + comm["bgm"] + "\n"
                
            else:
                rendu = rendu + deb + "commande inconnu : " + commande + "\n"
                print(rendu)
                error
                pass

    return rendu
getWrited(originalFile,to)
 
