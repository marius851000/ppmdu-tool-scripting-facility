import exportRead
import os
import shutil
import time
import sys

_debug = True
_stopOnError = False

def getWrited(original,to):
    if _debug:
        print(original)
    version = "0.1.3"
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
            print("can not make subdir")

    data = exportRead.getData(original)
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
        try:
            os.mkdir(subdir + "/" + pname)
        except:
            pass#TODO : research about this error
        nsub = subdir + "/" + pname
        temp = open(nsub + "/script.pms", "w")
        temp.write(toCode(loop))
        temp.close()

def toCode(fonction):
    rendu = ""
    deb = "    "
    for fonc in fonction["fonction"]:
        rendu = rendu + fonc["id"] + ":\n"
        for comm in fonc["funcl"]:
            #print(type(comm))
            #print(comm["commande"])
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
            elif commande == "lives":#lives
                rendu = rendu + deb + "lives " + comm["actorid"] + ":\n"
                for lcomm in comm["in"]:
                    print(lcomm)
                    lcommande = lcomm["lcommande"]
                    if lcommande == "turn2Direction":
                        rendu = rendu + deb + deb + "turn2Direction " + lcomm["param"] + ", " + lcomm["param_1"] + ", direction = " + lcomm["direction"] + "\n"
                    elif lcommande == "move2PositionMark":
                        rendu = rendu + deb + deb + "move2PositionMark " + lcomm["param"] + ", " + lcomm["param_2"] + ", " + lcomm["param_3"] + ", " + lcomm["param_4"] + "\n"
                    elif lcommande == "movePositionMark":
                        if lcomm["x"]==None or lcomm["y"]==None:
                            rendu = rendu + deb + deb + "movePositionMark " + lcomm["param"] + ", " + lcomm["param_2"] +  "\n"
                        else:
                            rendu = rendu + deb + deb + "movePositionMark " + lcomm["param"] + ", " + lcomm["param_2"] + ", x = " + lcomm["x"] + ", y = " + lcomm["y"] + "\n"
                    elif lcommande == "executeCommon":
                        rendu = rendu + deb + deb + "executeCommon croutineid = " + lcomm["croutineid"] + ", " + lcomm["param_1"] + "\n"
                    elif lcommande == "turn2DirectionLives":
                        rendu = rendu + deb + deb + "turn2DirectionLives " + lcomm["param"] + ", " + lcomm["param_1"] + ", actorid = " + lcomm["actorid"] + "\n"
                    elif lcommande == "setEffect":
                        rendu = rendu + deb + deb + "setEffect " + lcomm["param"] + ", " + lcomm["param_1"] + "\n"
                    elif lcommande == "waitEffect":
                        rendu = rendu + deb + deb + "waitEffect\n"
                    elif lcommande == "setAnimation":
                        rendu = rendu + deb + deb + "setAnimation animid = " + lcomm.get("animid") + "\n"
                    elif lcommande == "slidePositionMark":
                        rendu = rendu + deb + deb + "slidePositionMark " + lcomm["param"] + ", " + lcomm["param_2"] + ", " + lcomm["param_3"] + ", " + lcomm["param_4"] + "\n"
                    elif lcommande == "setFunctionAttribute":
                        rendu = rendu + deb + deb + "setFunctionAttribute " + lcomm["param"]+"\n"
                    elif lcommande == "setPositionMark":
                        rendu = rendu + deb + deb + "setPositionMark " + lcomm["param"] + ", " + lcomm["param_1"] + ", " + lcomm["param_2"] + ", " + lcomm["param_3"] + "\n"
                    elif lcommande == "setDirection":
                        rendu = rendu + deb + deb + "setDirection direction = " + lcomm["direction"] + "\n"
                    elif lcommande == "movePositionOffset":
                        if lcomm["x"]==None or lcomm["y"]==None:
                            rendu = rendu + deb + deb + "movePositionOffset " + lcomm["param"] + "\n"
                        else:
                            rendu = rendu + deb + deb + "movePositionOffset " + lcomm["param"] + ", x = " + lcomm["x"] + ", y = " + lcomm["y"] + "\n"
                    elif lcommande == "setPositionInitial":
                        rendu = rendu + deb + deb + "setPositionInitial\n"
                    elif lcommande == "waitAnimation":
                        rendu = rendu + deb + deb + "waitAnimation\n"
                    elif lcommande == "slidePositionOffset":
                        if lcomm["y"]==None and lcomm["x"]==None:
                            rendu = rendu + deb + deb + "slidePositionOffset " + lcomm["param"] + "\n"
                        else:
                            rendu = rendu + deb + deb + "slidePositionOffset " + lcomm["param"] + ", x = " + lcomm["x"] + ", y = " + lcomm["y"] + "\n"
                    elif lcommande == "move2PositionOffset":
                        if lcomm["x"]==None or lcomm["y"]==None:
                            rendu = rendu + deb + deb + "move2PositionOffset " + lcomm["param"] + "\n"
                        else:
                            rendu = rendu + deb + deb + "move2PositionOffset " + lcomm["param"] + ", x = " + lcomm["x"] + ", y = " + lcomm["y"] + "\n"
                    elif lcommande == "setOutputAttribute":
                        rendu = rendu + deb + deb + "setOutputAttribute " + lcomm["param"] + "\n"
                    elif lcommande == "resetHitAttribute":
                        rendu = rendu + deb + deb + "resetHitAttribute " + lcomm["param"] + "\n"
                    elif lcommande == "turn2DirectionTurn":
                        rendu = rendu + deb + deb + "turn2DirectionTurn " + lcomm["param"] + ", " + lcomm["param_1"] + ", " + lcomm["param_2"] + "\n"
                    elif lcommande == "slide2PositionOffset":
                        rendu = rendu + deb + deb + "slide2PositionOffset " + lcomm["param"] + ", x = " + lcomm["x"] + ", y = " + lcomm["y"] + "\n"
                    elif lcommande == "destroy":
                        rendu = rendu + deb + deb + "destroy\n"
                    elif lcommande == "resetOutputAttribute":
                        rendu = rendu + deb + deb + "resetOutputAttribute " + lcomm["param"] + "\n"
                    elif lcommande == "moveHeight":
                        rendu = rendu + deb + deb + "moveHeight " + lcomm["param"] + ", " + lcomm["param_1"] + "\n"
                    elif lcommande == "setPositionOffset":
                        rendu = rendu + deb + deb + "setPositionOffset " + lcomm["param"] + ", " + lcomm["param_1"] + "\n"
                    elif lcommande == "resetFunctionAttribute":
                        rendu = rendu + deb + deb + "resetFunctionAttribute " + lcomm["param"] + "\n"
                    elif lcommande == "moveposition":
                        rendu = rendu + deb + deb + "movePositionOffset " + lcomm["param"] + ", x = " + lcomm["x"] + ", y = " + lcomm["y"] + "\n"
                    elif lcommande == "turn3":
                        rendu = rendu + deb + deb + "turn3 " + lcomm["param"] + ", " + lcomm["param_1"] + ", " + lcomm["param_2"] + ", " + lcomm["param_3"] + "\n"
                    elif lcommand == "hold":
                        rendu = rendu + deb + deb + "hold\n"
                    elif lcommand == "setOutputAttributeAndAnimation":
                        rendu = rendu + deb + deb + "setOutputAttributeAndAnimation " + lcomm["param"] + ", " + lcomm["param_1"] + ", " + lcomm["param_2"] + "\n"
                    elif lcommande == "pursueTurnLives":
                        rendu = rendu + deb + deb + "pursueTurnLives " + lcomm["param"] + ", " + lcomm["param_1"] + ", " + lcomm["param_2"] + ", " + lcomm["param_3"] + "\n"
                    elif lcommande == "pursueTurnLives2":
                        rendu = rendu + deb + deb + "pursueTurnLives2 " + lcomm["param"] + ", " + lcomm["param_1"] + ", " + lcomm["param_2"] + ", " + lcomm["param_3"] + "\n"
                    elif lcommand == "endAnimation":
                        rendu = rendu + deb + deb + "endAnimation\n"
                    elif lcommand == "setBlink":
                        rendu = rendu + deb + deb + "setBlink " + lcomm["param"] + ", " + lcomm["param_1"] + "\n"

                    else:
                        rendu = rendu + deb + deb + "live inconnu\n"
                        print("erreur : live non traité : " + lcommande)
                        print(lcomm)
                        if _stopOnError:
                            errore()


            elif commande == "messageClose":
                rendu = rendu + deb + "messageClose\n"
            elif commande == "messageSwitchTalk":
                rendu = rendu + deb + "messageSwitchTalk " + comm["svar"] + ":\n"
                for loop in comm["case"]:
                    if loop["type"]=="int":
                        rendu = rendu + deb + deb + "case " + loop["value"] + ":\n"
                        for loop2 in loop["text"]:
                            rendu = rendu + deb + deb + deb + loop2[0] + " = \"\"\"" + loop2[1] + "\"\"\"\n"
                    else:
                        print("erreur : type non spécifié")
                        if _stopOnError:
                            errore()
                rendu = rendu + deb + deb + "default:\n"
                for loop in comm["default"]:
                    rendu = rendu + deb + deb + deb + loop[0] + " = \"\"\"" + loop[1] + "\"\"\"\n"
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
                rendu = rendu + deb + "waitScreenFadeAll\n"
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
                    rendu = rendu + deb + deb + loop[0] + " = \"\"\"" + loop[1] + "\"\"\"\n"
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
                rendu = rendu + deb + "backSetBanner2 " + comm["param"] + ", " + comm["param_1"] + ", x = " + comm["x"] + ", y = " + comm["y"] + ", " + comm["param_4"] + "\n" # REVIEW:
            elif commande == "flagSetScenario":
                rendu = rendu + deb + "flagSetScenario svar = " + comm["svar"] + ", " + comm["param_1"] + ", " + comm["param_2"] + "\n"
            elif commande == "messageSwitchMonologue":
                rendu = rendu + deb + "messageSwitchMonologue " + comm["svar"] + ":\n"
                for loop in comm["case"]:
                    if loop["type"]=="int":
                        rendu = rendu + deb + deb + "case " + loop["value"] + ":\n"
                        for loop2 in loop["text"]:
                            rendu = rendu + deb + deb + deb + loop2[0] + " = \"\"\"" + loop2[1] + "\"\"\"\n"
                    else:
                        print("erreur : type non spécifié")
                        if _stopOnError:
                            errore()
                rendu = rendu + deb + deb + "default:\n"
                for loop in comm["default"]:
                    rendu = rendu + deb + deb + deb + loop[0] + " = \"\"\"" + loop[1] + "\"\"\"\n"
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
            elif commande == "messageNotice":
                rendu = rendu + deb + "messageNotice:\n"
                for loop in comm["text"]:
                    rendu = rendu + deb + deb + loop[0] + " = \"\"\"" + loop[1] + "\"\"\"\n"
            elif commande == "supervisionExecuteStation":
                rendu = rendu + deb + "supervisionExecuteStation level = " + comm["levelid"] + ", constref = " + comm["constref"] + ", " + comm["param_2"] + "\n"
            elif commande == "hold":
                rendu = rendu + deb + "hold\n"
            elif commande == "branchBit":
                rendu = rendu + deb + "branchBit svar = " + comm["svar"] + ", " + comm["param_1"] + ", label = " + comm["tolabel"] + "\n"
            elif commande == "branchScenarioBefore":
                rendu = rendu + deb + "branchScenarioBefore svar = " + comm["svar"] + ", " + comm["param_1"] + ", " + comm["param_2"] + ", label = " + comm["tolabel"] + "\n"
            elif commande == "BranchScenarioNow":
                rendu = rendu + deb + "BranchScenarioNow svar = " + comm["svar"] + ", " + comm["param_1"] + ", " + comm["param_2"] + ", label = " + comm["tolabel"] + "\n"
            elif commande == "processSpecial":
                rendu = rendu + deb + "processSpecial procspec = " + comm["procspec"] + ", " + comm["param_1"] + ", " + comm["param_2"] + "\n"
            elif commande == "supervisionExecuteStationSub":
                rendu = rendu + deb + "supervisionExecuteStationSub level = " + comm["levelid"] + ", constref = " + comm["constref"] + ", " + comm["param_2"] + "\n"
            elif commande == "switchScenario":
                rendu = rendu + deb + "switchScenario svar = " + comm["svar"] + ":\n"
                rendu = rendu + deb + deb + "TODO\n"#TODO : in
            elif commande == "BranchScenarioNowAfter":
                rendu = rendu + deb + "BranchScenarioNowAfter svar = " + comm["svar"] + ", " + comm["param_1"] + ", " + comm["param_2"] + ", label = " + comm["tolabel"] + "\n"
            elif commande == "waitSubScreen":
                rendu = rendu + deb + "waitSubScreen\n"
            elif commande == "waitFadeIn":
                rendu = rendu + deb + "waitFadeIn\n"
            elif commande == "messageMonologue":
                rendu = rendu + deb + "messageMonologue:\n"
                for loop in comm["text"]:
                    rendu = rendu + deb + deb + loop[0] + " = \"\"\"" + loop[1] + "\"\"\"\n"
            elif commande == "screenFadeChange":
                rendu = rendu + deb + "screenFadeChange " + comm["param"] + ", " + comm["param_1"] + ", " + comm["param_2"] + ", " + comm["param_3"] + "\n"
            elif commande == "bgmChangeVolume":
                rendu = rendu + deb + "bgmChangeVolume duration = " + comm["duration"] + ", volume = " + comm["vol"] + "\n"
            elif commande == "bgm2PlayFadeIn":
                rendu = rendu + deb + "bgm2PlayFadeIn bgm = " + comm["bgm"] + ", duration = " + comm["duration"] + ", volume = " + comm["vol"] + "\n"
            elif commande == "messageMail":
                rendu = rendu + deb + "messageMail:\n"
                for loop in comm["text"]:
                    rendu = rendu + deb + deb + loop[0] + " = \"\"\"" + loop[1]+ "\"\"\"\n"
            elif commande == "bgm2FadeOut":
                rendu = rendu + deb + "bgm2FadeOut " + comm["param"] + "\n"
            elif commande == "waitBgm2":
                rendu = rendu + deb + "waitBgm2 " + comm["param"] + "\n"
            elif commande == "messageKeyWait":
                rendu = rendu + deb + "messageKeyWait\n"
            elif commande == "back2SetEffect":
                rendu = rendu + deb + "back2SetEffect " + comm["param"] + ", " + comm["param_1"] + "\n"
            elif commande == "flagCalcBit":
                rendu = rendu + deb + "flagCalcBit svar = " + comm["svar"] + ", " + comm["param_1"] + ", " + comm["param_2"] + "\n"
            elif commande == "mePlay":
                rendu = rendu + deb + "mePlay " + comm["param"] + "\n"
            elif commande == "messageExplanation":
                rendu = rendu + deb + "messageExplanation:\n"
                for loop in comm["text"]:
                    rendu = rendu + deb + deb + loop[0] + " = \"\"\"" + loop[1]+ "\"\"\"\n"
            elif commande == "flagSet":
                rendu = rendu + deb + "flagSet to = " + comm["to"] + ", type = " + comm["type"] + "\n"
            elif commande == "messageSwitchMenu":
                rendu = rendu + deb + "messageSwitchMenu " + comm["param"] + ", " + comm["param_1"] + ":\n"
                for loop in comm["lcase"]:
                    if loop[0] == "normal":
                        rendu = rendu + deb + deb + loop[1] + ":\n"
                        for loop2 in loop[2]:
                            rendu = rendu + deb + deb + deb + loop2[0] + " = " + loop2[1] + "\n"
                    elif loop[0] == "ex":
                        rendu = rendu + deb + deb + "TODO:"
            elif commande == "backSetBackEffect":
                rendu = rendu + deb + "backSetBackEffect " + comm["param"] + "\n"
            elif commande == "screenWhiteOut":
                if comm["bool"] == "1":
                    boole = "True"
                else:
                    boole = "False"
                rendu = rendu + deb + "screenWhiteOut duration = " + comm["duration"] + ", bool = " + boole + "\n"
            elif commande == "messageCloseEnforce":
                rendu = rendu + deb + "messageCloseEnforce\n"
            elif commande == "messageNarration":
                rendu = rendu + deb + "messageNarration " + comm["param"] + ":\n"
                for loop in comm["text"]:
                    rendu = rendu + deb + deb + loop[0] + " = \"\"\"" + loop[1]+ "\"\"\"\n"
            elif commande == "supervisionLoadStation":
                rendu = rendu + deb + "supervisionLoadStation level = " + comm["levelid"] + ", constref = " + comm["constref"] + "\n"
            elif commande == "supervisionStation":
                rendu = rendu + deb + "supervisionStation station = " + comm["stationid"] + "\n"
            elif commande == "supervisionSpecialActing":
                rendu = rendu + deb + "supervisionSpecialActing " + comm["param"] + ", " + comm["param_1"] + ", " + comm["param_2"] + "\n"
            elif commande == "supervision2SpecialActing":
                rendu = rendu + deb + "supervision2SpecialActing " + comm["param"] + ", " + comm["param_1"] + ", " + comm["param_2"] + "\n"
            elif commande == "messageMenu":
                rendu = rendu + deb + "messageMenu " + comm["menuid"] + "\n"
            elif commande == "bgm2Stop":
                rendu = rendu + deb + "bgm2Stop\n"
            elif commande == "messageFacePositionOffset":
                rendu = rendu + deb + "messageFacePositionOffset x = " + comm["x"] + ", y = " + comm["y"] + "\n"
            elif commande == "mainEnterDungeon":
                rendu = rendu + deb + "mainEnterDungeon " + comm["param"] + ", " + comm["param_1"] + "\n"
            elif commande == "waitLockLives":
                rendu = rendu + deb + "waitLockLives " + comm["param"] + ", " + comm["param_1"] + "\n"
            elif commande == "unlock":
                rendu = rendu + deb + "unlock " + comm["param"] + "\n"
            elif commande == "lock":
                rendu = rendu + deb + "lock " + comm["param"] + "\n"
            elif commande == "setDirection":
                rendu = rendu + deb + "setDirection " + comm["direction"] + "\n"
            elif commande == "back2SetBackEffect":
                rendu = rendu + deb + "back2SetBackEffect " + comm["param"] + "\n"
            elif commande == "screen2WhiteOut":
                if comm["bool"] == "1":
                    boole = "True"
                else:
                    boole = "False"
                rendu = rendu + deb + "screen2WhiteOut duration = " + comm["duration"] + ", bool = " + boole + "\n"
            elif commande == "flagClear":
                rendu = rendu + deb + "flagClear " + comm["svar"] + "\n"
            elif commande == "bgm2ChangeVolume":
                rendu = rendu + deb + "bgm2ChangeVolume " + comm["param"] + ", " + comm["param_1"] + "\n"
            elif commande == "flagCalcValue":
                rendu = rendu + deb + "flagCalcValue svar = " + comm["svar"] + ", " + comm["param_1"] + ", int = " + comm["int"] + "\n"
            elif commande == "messageSetWaitMode":
                rendu = rendu + deb + "messageSetWaitMode " + comm["param"] + ", " + comm["param_1"] + "\n"
            elif commande == "setOutputAttribute":
                rendu = rendu + deb + "setOutputAttribute " + comm["param"] + "\n"
            elif commande == "slidePositionOffset":
                rendu = rendu + deb + "SlidePositionOffset " + comm["param"] + ", x = " + comm["x"] + ", " + comm["y"] + "\n"
            elif commande == "setEffect":
                rendu = rendu + deb + "SetEffect " + comm["param"] + ", " + comm["param_1"] + "\n"
            elif commande == "waitAnimation":
                rendu = rendu + deb + "WaitAnimation\n"
            elif commande == "turn2Direction":
                rendu = rendu + deb + "Turn2Direction " + comm["param"] + ", " + comm["param_1"] + ", direction = " + comm["direction"] + "\n"
            elif commande == "waitBgmSignal":
                rendu = rendu + deb + "WaitBgmSignal\n"
            elif commande == "waitEffect":
                rendu = rendu + deb + "WaitEffect\n"
            elif commande == "slidePositionOffset":
                rendu = rendu + deb + "slidePositionOffset " + comm["param"] + ", x = " + comm["x"] + ", y = " + comm["y"] + "\n"
            elif commande == "setPositionOffset":
                rendu = rendu + deb + "setPositionOffset " + comm["param"] + ", " + comm["param_1"] + "\n"
            elif commande == "backSetDungeonBanner":
                rendu = rendu + deb + "backSetDungeonBanner " + comm["param"] + ", " + comm["param_1"] + "\n"
            elif commande == "bgmStop":
                rendu = rendu + deb + "bgmStop\n"
            elif commande == "branchPerformance":
                rendu = rendu + deb + "branchPerformance " + comm["param"] + ", " + comm["param_1"] + ", " + comm["param_2"] + "\n"
            elif commande == "branchVariation":
                rendu = rendu + deb + "branchVariation svar = " + comm["svar"] + ", label = " + comm["tolabel"] + "\n"
            elif commande == "switchScenarioLevel":
                rendu = rendu + deb + "switchScenarioLevel " + comm["svar"] + ":\n"
                rendu = rendu + deb + deb + "TODO\n" #TODO : in
            elif commande == "movePositionMark":
                rendu = rendu + deb + "movePositionMark " + comm["param"] + ", " + comm["param_1"] + ", " + comm["param_2"] + ", x = " + comm["x"] + ", y = " + comm["y"] + "\n"
            elif commande == "screenWhiteOutAll":
                rendu = rendu + deb + "screenWhiteOutAll " + comm["param"] + ", " + comm["param_1"] + "\n"
            elif commande == "screenFadeInAll":
                if comm["bool"] == "1":
                    boole = "True"
                else:
                    boole = "False"
                rendu = rendu + deb + "screenFadeInAll duration = " + comm["duration"] + ", bool = " + boole + "\n"
            elif commande == "seFadeOut":
                rendu = rendu + deb + "seFadeOut " + comm["param"] + ", " + comm["param_1"] + "\n"
            elif commande == "setPositionInitial":
                rendu = rendu + deb + "setPositionInitial\n"
            elif commande == "supervisionExecuteCommon":
                rendu = rendu + deb + "supervisionExecuteCommon " + comm["croutineid"] + "\n"
            elif commande == "branch":
                rendu = rendu + deb + "branch svar = " + comm["svar"] + ", " + comm["param_1"] + ", label = " + comm["tolabel"] + "\n"
            elif commande == "cameraMove2Default":
                rendu = rendu + deb + "cameraMove2Default " + comm["param"] + "\n"
            elif commande == "supervisionSuspend":
                rendu = rendu + deb + "supervisionSuspend " + comm["param"] + "\n"
            elif commande == "messageImitationSound":
                rendu = rendu + deb + "messageImitationSound:\n"
                for loop in comm["text"]:
                    rendu = rendu + deb + deb + loop[0] + " = \"\"\"" + loop[1] + "\"\"\"\n"
            elif commande == "waitMe":
                rendu = rendu + deb + "waitMe " + comm["param"] + "\n"
            elif commande == "worldmapSetMode":
                rendu = rendu + deb + "worldmapSetMode " + comm["param"] + "\n"
            elif commande == "worldmapSetLevel":
                rendu = rendu + deb + "worldmapSetLevel " + comm["param"] + "\n"
            elif commande == "worldmapChangeLevel":
                rendu = rendu + deb + "worldmapChangeLevel " + comm["param"] + "\n"
            elif commande == "worldmapSetCamera":
                rendu = rendu + deb + "worldmapSetCamera " + comm["param"] + "\n"
            elif commande == "resetFunctionAttribute":
                rendu = rendu + deb + "resetFunctionAttribute " + comm["param"] + "\n"
            elif commande == "slidePositionMark":
                rendu = rendu + deb + "slidePositionMark " + comm["param"] + ", " + comm["param_1"] + ", " + comm["param_2"] + ", " + comm["param_3"] + ", " + comm["param_4"] + "\n"
            elif commande == "setFunctionAttribute":
                rendu = rendu + deb + "setFunctionAttribute " + comm["param"] + "\n"
            elif commande == "slideHeight":
                rendu = rendu + deb + "slideHeight " + comm["param"] + ", " + comm["param_1"] + "\n"
            elif commande == "mainSetGround":
                rendu = rendu + deb + "mainSetGround " + comm["levelid"] + "\n"
            elif commande == "mainEnterGround":
                rendu = rendu + deb + "mainEnterGround level = " + comm["levelid"] + ", " + comm["param_1"] + "\n"
            elif commande == "supervisionRemoveCommon":
                rendu = rendu + deb + "supervisionRemoveCommon " + comm["param"] + "\n"
            elif commande == "slide2PositionMark":
                rendu = rendu + deb + "slide2PositionMark " + comm["param"] + ", " + comm["param_1"] + ", " + comm["param_2"] + ", " + comm["param_3"] + ", " + comm["param_4"] + "\n"
            elif commande == "flagSetPerformance":
                rendu = rendu + deb + "flagSetPerformance " + comm["param"] + ", " + comm["param_1"] + "\n"
            elif commande == "moveHeight":
                rendu = rendu + deb + "moveHeight " + comm["param"] + ", " + comm["param_1"] + "\n"
            elif commande == "branchDebug":
                rendu = rendu + deb + "branchDebug label = " + comm["tolabel"] + ", bool = " + comm["bool"] + "\n" #TODO : boole
            elif commande == "waitScreen2Fade":
                rendu = rendu + deb + "waitScreen2Fade\n"
            elif commande == "screenWhiteChange":
                rendu = rendu + deb + "screenWhiteChange " + comm["param"] + ", " + comm["param_1"] + ", " + comm["param_2"] + ", " + comm["param_3"] + "\n"
            elif commande == "messageSetFaceEmpty":
                rendu = rendu + deb + "messageSetFaceEmpty " + comm["param"] + ", " + comm["param_1"] + ", " + comm["param_2"] + "\n"
            elif commande == "worldmapSetArrow":
                rendu = rendu + deb + "worldmapSetArrow " + comm["param"] + "\n"
            elif commande == "worldmapBlinkMark":
                rendu = rendu + deb + "worldmapBlinkMark " + comm["param"] + "\n"
            elif commande == "switchRandom":
                rendu = rendu + deb + "switchRandom " + comm["param"] + ":\n"
                rendu = rendu + deb + deb + "TODO" #TODO
            elif commande == "supervisionExecuteStationCommon":
                rendu = rendu + deb + "supervisionExecuteStationCommon level = " + comm["levelid"] + ", " + comm["param_1"] + "\n"
            elif commande == "setMoveRange":
                rendu = rendu + deb + "setMoveRange " + comm["param"] + ", " + comm["param_1"] + ", " + comm["param_2"] + ", " + comm["param_3"] + ", " + comm["param_4"] + ", " + comm["param_5"] + "\n"
            elif commande == "sePlayVolume":
                rendu = rendu + deb + "sePlayVolume " + comm["param"] + ", " + comm["param_1"] + "\n"
            elif commande == "seChangeVolume":
                rendu = rendu + deb + "seChangeVolume " + comm["param"] + ", " + comm["param_1"] + ", " + comm["param_2"] + "\n"
            elif commande == "waitRandom":
                rendu = rendu + deb + "waitRandom " + comm["param"] + ", " + comm["param_1"] + "\n"
            elif commande == "movePositionOffset":
                rendu = rendu + deb + "#movePositionOffset - TODO\n" #TODO : condition
                #rendu = rendu + deb + "movePositionOffset " + comm["param"] + ", x = " + comm["x"] + ", y = " + comm["y"] + "\n"
            elif commande == "camera2SetEffect":
                rendu = rendu + deb + "camera2SetEffect " + comm["param"] + ", " + comm["param_1"] + ", " + comm["param_2"] + "\n"
            elif commande == "slide2PositionLives":
                rendu = rendu + deb + "slide2PositionLives " + comm["param"] + ", " + comm["param_1"] + "\n"
            elif commande == "supervisionActingInvisible":
                rendu = rendu + deb + "supervisionActingInvisible " + comm["layerid"] + "\n"
            elif commande == "resetOutputAttribute":
                rendu = rendu + deb + "resetOutputAttribute " + comm["param"] + "\n"
            elif commande == "backSetEffect":
                rendu = rendu + deb + "backSetEffect " + comm["param"] + ", " + comm["param_1"] + "\n"
            elif commande == "waitBackEffect":
                rendu = rendu + deb + "waitBackEffect\n"
            elif commande == "waitEndAnimation":
                rendu = rendu + deb + "waitEndAnimation\n"
            elif commande == "turn2DirectionLives":
                rendu = rendu + deb + "turn2DirectionLives " + comm["param"] + ", " + comm["param_1"] + ", actor " + comm["actorid"] + "\n"
            elif commande == "move2PositionLives":
                rendu = rendu + deb + "move2PositionLives " + comm["param"] + ", " + comm["param_1"] + "\n"
            elif commande == "cameraSetDefault":
                rendu = rendu + deb + "cameraSetDefault\n"
            elif commande == "destroy":
                rendu = rendu + deb + "destroy\n"
            elif commande == "stopAnimation":
                rendu = rendu + deb + "stopAnimation\n"
            elif commande == "itemSet":
                rendu = rendu + deb + "itemSet " + comm["param"] + ", item = " + comm["itemid"] + ", " + comm["param_2"] + "\n"
            elif commande == "branchScenarioNowBefore":
                rendu = rendu + deb + "branchScenarioNowBefore svar = " + comm["svar"] + ", " + comm["param_1"] + ", " + comm["param_2"] + ", label = " + comm["tolabel"] + "\n"
            elif commande == "itemSetTableData":
                rendu = rendu + deb + "itemSetTableData " + comm["param"] + ", " + comm["param_1"] + "\n"
            elif commande == "backSetWeather":
                rendu = rendu + deb + "backSetWeather " + comm["param"] + "\n"
            elif commande == "pauseEffect":
                rendu = rendu + deb + "pauseEffect " + comm["param"] + "\n"
            elif commande == "supervisionExecuteActing":
                rendu = rendu + deb + "supervisionExecuteActing level = " + comm["levelid"] + ", constref = " + comm["constref"] + ", " + comm["param_2"] + "\n"
            elif commande == "bgm2Play":
                rendu = rendu + deb + "bgm2Play " + comm["bgm"] + "\n"
            elif commande == "resetHitAttribute":
                rendu = rendu + deb + "resetHitAttribute " + comm["param"] + "\n"
            elif commande == "backChangeGround":
                rendu = rendu + deb + "backChangeGround " + comm["levelid"] + "\n"
            elif commande == "cameraSetMyPosition":
                rendu = rendu + deb + "cameraSetMyPosition\n"
            elif commande == "worldmapSetMark":
                rendu = rendu + deb + "worldmapSetMark " + comm["param"] + "\n"
            elif commande == "worldmapMoveCamera":
                rendu = rendu + deb + "worldmapMoveCamera " + comm["param"] + "\n"
            elif commande == "worldmapSetMessagePlace":
                rendu = rendu + deb + "worldmapSetMessagePlace " + comm["param"] + "\n"
            elif commande == "mainEnterAdventure":
                rendu = rendu + deb + "mainEnterAdventure " + comm["param"] + ", " + comm["param_1"] + "\n"
            elif commande == "cameraMoveDefault":
                rendu = rendu + deb + "cameraMoveDefault " + comm["param"] + "\n"
            elif commande == "screen2WhiteChange":
                rendu = rendu + deb + "screen2WhiteChange " + comm["param"] + ", " + comm["param_1"] + ", " + comm["param_2"] + ", " + comm["param_3"] + "\n"
            elif commande == "backSetBackScrollSpeed":
                rendu = rendu + deb + "backSetBackScrollSpeed " + comm["param"] + ", " + comm["param_1"] + "\n"
            elif commande == "move2PositionMark":
                rendu = rendu + deb + "move2PositionMark " + comm["param"] + ", " + comm["param_1"] + ", " + comm["param_2"] + ", " + comm["param_3"] + ", " + comm["param_4"] + "\n"
            elif commande == "setPositionMark":
                rendu = rendu + deb + "setPositionMark " + comm["param"] + ", " + comm["param_1"] + ", " + comm["param_2"] + ", " + comm["param_3"]+"\n"
            elif commande == "back2SetBackScrollSpeed":
                rendu = rendu + deb + "back2SetBackScrollSpeed " + comm["param"] + ", " + comm["param_1"] + "\n"
            elif commande == "waitLockObject":
                rendu = rendu + deb + "waitLockObject " + comm["param"] + ", " + comm["param_1"] + "\n"
            elif commande == "turn3":
                rendu = rendu + deb + "turn3 " + comm["param"] + ", " + comm["param_1"] + ", " + comm["param_2"] + ", " + comm["param_3"] + "\n"
            elif commande == "camera2MovePositionMark":
                rendu = rendu + deb + "camera2MovePositionMark " + comm["param"] + ", " + comm["param_1"] + ", " + comm["param_2"] + ", " + comm["param_3"] + ", " + comm["param_4"] + "\n"
            elif commande == "waitMoveCamera2":
                rendu = rendu + deb + "waitMoveCamera2\n"
            elif commande == "worldmapDeleteArrow":
                rendu = rendu + deb + "worldmapDeleteArrow\n"
            elif commande == "waitMoveCamera":
                rendu = rendu + deb + "waitMoveCamera\n"
            elif commande == "flagSetAdventureLog":
                rendu = rendu + deb + "flagSetAdventureLog " + comm["param"] + "\n"
            elif commande == "itemGetVariable":
                rendu = rendu + deb + "itemGetVariable " + comm["param"] + ", " + comm["param_1"] + "\n"
            elif commande == "backSetSpecialEpisodeBanner3":
                rendu = rendu + deb + "backSetSpecialEpisodeBanner3:\n"
                for loop in comm["text"]:
                    rendu = rendu + deb + deb + loop[0] + " = \"\"\"" + loop[1] + "\"\"\"\n"
            elif commande == "backSetSpecialEpisodeBanner":
                rendu = rendu + deb + "backSetSpecialEpisodeBanner:\n"
                for loop in comm["text"]:
                    rendu = rendu + deb + deb + loop[0] + " = \"\"\"" + loop[1] + "\"\"\"\n"
            elif commande == "backSetSpecialEpisodeBanner2":
                rendu = rendu + deb + "backSetSpecialEpisodeBanner2:\n"
                for loop in comm["text"]:
                    rendu = rendu + deb + deb + loop[0] + " = \"\"\"" + loop[1] + "\"\"\"\n"
            elif commande == "backSetBackScrollOffset":
                rendu = rendu + deb + "backSetBackScrollOffset " + comm["param"] + ", " + comm["param_1"] + "\n"
            elif commande == "cameraSetMyself":
                rendu = rendu + deb + "cameraSetMyself\n"
            elif commande == "cameraMove2PositionMark":
                rendu = rendu + deb + "cameraMove2PositionMark " + comm["param"] + ", " + comm["param_1"] + ", " + comm["param_2"] + ", " + comm["param_3"] + ", " + comm["param_4"] + ", " + comm["param_5"] + ", " + comm["param_6"] + ", " + comm["param_7"] + ", " + comm["param_8"] + ", " + comm["param_9"] + ", " +  comm["param_10"] + ", " +  comm["param_11"] + ", " + comm["param_12"] + ", " + comm["param_13"] + ", " + comm["param_14"] + ", " + comm["param_15"] + ", " + comm["param_16"] + "\n"
            elif commande == "slide2PositionOffset":
                rendu = rendu + deb + "slide2PositionOffset " + comm["param"] + ", y = " + comm["y"] + ", x = " + comm["x"] + "\n"
            elif commande == "move3PositionOffset":
                rendu = rendu + deb + "slide2PositionOffset " + comm["param"] + ", y = " + comm["y"] + ", x = " + comm["x"] + "\n"
            elif commande == "moveTurn":
                rendu = rendu + deb + "moveTurn " + comm["param"] + ", " + comm["param_1"] + ", " + comm["param_2"] + "\n"
            elif commande == "turn2directionLives2":
                rendu = rendu + deb + "turn2directionLives2 " + comm["param"] + "," + comm["param_1"] + "," + comm["param_2"] + "\n"
            elif commande == "waitLockSupervision":
                rendu = rendu + deb + "waitLockSupervision " + comm["param"] + "\n"
            elif commande == "moveSpecial":
                rendu = rendu + deb + "moveSpecial " + comm["param"] + "," + comm["param_1"] + "," + comm["param_2"] + "\n"
            elif commande == "call":
                rendu = rendu + deb + "call lroutineid " + comm["lroutineid"] + "\n"
            elif commande == "return":
                rendu = rendu + deb + "return\n"
            elif commande == "slide3PositionOffset":
                rendu = rendu + deb + "slide3PositionOffset " + comm["param"] + ", y = " + comm["y"] + ", x = " + comm["x"] + "\n"
            elif commande == "back2SetWeather":
                rendu = rendu + deb + "back2SetWeather " + comm["param"] + "\n"
            elif commande == "backSetBanner":
                rendu = rendu + deb + "backSetBanner " + comm["param"] + ":\n"# TODO: multiple
            elif commande == "backSetTitleBanner":
                rendu = rendu + deb + "backSetTitleBanner " + comm["param"] + ":\n"# TODO: multiple
            elif commande == "backSetWeatherEffect":
                rendu = rendu + deb + "backSetWeatherEffect " + comm["param"] + "\n"
            elif commande == "worldmapOffMessage":
                rendu = rendu + deb + "worldmapOffMessage\n"
            elif commande == "moveDirection":
                rendu = rendu + deb + "moveDirection " + comm["param"] + ", " + comm["param_1"] + ", " + comm["param_2"] + "\n"

            else:
                print("erreur : commande inconnu : " + commande)
                if _stopOnError:
                    errore()
                #error
                pass

    return rendu
if __name__ == "__main__":
    #TODO : scan de COMMON.xml
    #shutil.rmtree("rendu")
    try:
        load = open("salut.txt")
        a = load.read()
        load.close()
        a = a.split("\n")
        print(a)
    except:
        a = []
    try:
        os.mkdir("rendu")
    except:
        pass
    to = "rendu/"

    listeDuDir = os.listdir("export/scripts/")
    lenlisteDuDir = len(listeDuDir)
    counter = 0
    if True:
        for loop in listeDuDir:
            print(str(counter) + "/" + str(lenlisteDuDir))
            counter = counter + 1
            if loop != "COMMON.xml":
                getWrited("export/scripts/"+loop,to)
    else:
        getWrited("export/scripts/D10P41A.xml",to)
