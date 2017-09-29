import exportRead
import os
import shutil
import time

def getWrited(original,to):
    version = "0.0.2.2"#objectif : list all code, then, goto 0.1.x
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
                            rendu = rendu + deb + deb + deb + loop2[0] + " = \"\"\"" + loop2[1] + "\"\"\"\n"
                    else:
                        print("erreur : type non spécifié")
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
                rendu = rendu + deb + "backSetBanner2 " + comm["param"] + ", " + comm["param_1"] + ", x = " + comm["x"] + ", y = " + comm["y"] + ", " + comm["param_4"] + "\n"
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
            else:
                print("commande inconnu : " + commande)
                error
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

    for loop in os.listdir("export/scripts/"):
        if loop != "COMMON.xml":
            getWrited("export/scripts/"+loop,to)
