from lxml import etree
def getData(file):
    uncompilerversion = "0.2.0"
    temp = open(file,"r")
    xml = temp.read()
    temp.close()

    xmlt=""
    inCom=False
    for loop in range(len(xml)):
        if inCom == False:
            if xml[loop] == "<" and xml[loop+1] == "!" and xml[loop+2] == "-" and xml[loop+3] == "-":
                inCom = True
        else:
            if xml[loop-1] == ">" and xml[loop-2] == "-" and xml[loop-3] == "-":
                inCom = False

        if not inCom:
            xmlt = xmlt + xml[loop]


    root = etree.fromstring(xmlt)

    main = root[0]
    leveldata = { "version" : root.get("gameVersion"),
                  "region" : root.get("gameRegion")}

    scriptPack = []
    for scriptset in root:
        if scriptset.tag == "LSDTable":
            LSDdata = []
            for ref in scriptset:
                LSDdata.append(ref.get("name"))

        elif scriptset.tag == "ScriptSet":
            name = scriptset.get("name")
            #TODO : triggerTable
            #TODO : position marker
            #TODO : Layer
            script = scriptset[1]
            scriptName = script.get("name")
            code = script[0]
            fonc = []
            for function in code:
                funcid = function.get("_id")
                funcl = []
                for command in function:
                    tag = command.tag
                    if tag == "sound_Stop":
                        funcl.append({"commande" : "soundStop"})
                    elif tag == "back2_SetMode":
                        obj = {"commande" : "back2SetMode",
                               "param" : command.get("param")}
                        funcl.append(obj)
                    elif tag == "back2_SetGround":
                        obj = {"commande" : "back2SetGround",
                               "levelid" : command.get("levelid")}
                        funcl.append(obj)
                    elif tag == "back_SetGround":
                        obj = {"commande" : "backSetGround",
                               "levelid" : command.get("levelid")}
                        funcl.append(obj)
                    elif tag == "supervision_StationCommon":
                        obj = {"commande" : "supervisionStationCommon",
                               "stationid" : command.get("stationid")}
                        funcl.append(obj)
                    elif tag == "supervision_Acting":
                        obj = {"commande" : "supervisionActing",
                               "layerid" : command.get("layerid")}
                        funcl.append(obj)
                    elif tag == "performer":
                        obj = {"commande" : "performer",
                               "performerid" : command.get("performerid"),
                               "in" : "TODO"}#TODO : in
                        funcl.append(obj)
                    elif tag == "bgm_PlayFadeIn":
                        obj = {"commande" : "bgmPlayFadeIn",
                               "bgm" : command.get("bgm"),
                               "duration" : command.get("duration"),
                               "vol" : command.get("vol")}
                        funcl.append(obj)
                    elif tag == "screen2_FadeIn":
                        obj = {"commande" : "screen2FadeIn",
                               "bool" : command.get("bool"),
                               "duration" : command.get("duration")}
                        funcl.append(obj)
                    elif tag == "screen_FadeIn":
                        obj = {"commande" : "screenFadeIn",
                               "bool" : command.get("bool"),
                               "duration" : command.get("duration")}
                        funcl.append(obj)
                    elif tag == "Wait":
                        obj = {"commande" : "wait",
                               "duration" : command.get("duration")}
                        funcl.append(obj)
                    elif tag == "message_SetFace":
                        obj = {"commande" : "messageSetFace",
                               "actorid" : command.get("actorid"),
                               "face" : command.get("face"),
                               "facemode" : command.get("facemode")}
                        funcl.append(obj)
                    elif tag == "message_SwitchTalk":
                        caseText = []
                        defaultText = None
                        for case in command:
                            caset = []
                            for lang in case:
                                caset.append([lang.get("language"),lang.text])
                            if case.tag == "CaseText":
                                caseText.append({"type" : case.keys()[0],
                                                 "value" : case.get(case.keys()[0]),
                                                 "text" : caset})
                            elif case.tag == "DefaultText":
                                defaultText = caset
                            else:
                                print("erreur non bloquante : type de condition de texte non definie.")
                        obj = {"commande" : "messageSwitchTalk",
                               "svar" : command.get("svar"),
                               "case" : caseText,
                               "default" : defaultText}
                        funcl.append(obj)
                    elif tag == "CallCommon":
                        obj = {"commande" : "callCommon",
                               "croutineid" : command.get("croutineid")}
                        funcl.append(obj)
                    elif tag == "lives":
                        inlive = []
                        for lcommand in command:
                            ltag = lcommand.tag
                            if ltag == "Turn2Direction":
                                inlive.append({"lcommande":"turn2Direction",
                                    "param" : lcommand.get("param"),
                                    "param_1" : lcommand.get("param_1"),
                                    "direction" : lcommand.get("direction")})
                            elif ltag == "Move2PositionMark":
                                inlive.append({"lcommande":"move2PositionMark",
                                    "param" : lcommand.get("param"),
                                    "param_1" : lcommand.get("param_1"),
                                    "param_2" : lcommand.get("param_2"),
                                    "param_3" : lcommand.get("param_3"),
                                    "param_4" : lcommand.get("param_4")})
                            elif ltag == "MovePositionMark":
                                inlive.append({"lcommande":"movePositionMark",
                                    "param" : lcommand.get("param"),
                                    "param_1" : lcommand.get("param_1"),
                                    "param_2" : lcommand.get("param_2"),
                                    "x" : lcommand.get("x"),
                                    "y" : lcommand.get("y")})
                            elif ltag == "ExecuteCommon":
                                inlive.append({"lcommande" : "executeCommon",
                                    "croutineid" : lcommand.get("croutineid"),
                                    "param_1" : lcommand.get("param_1")})
                            elif ltag == "Turn2DirectionLives":
                                inlive.append({"lcommande" : "turn2DirectionLives",
                                    "param" : lcommand.get("param"),
                                    "param_1" : lcommand.get("param_1"),
                                    "actorid" : lcommand.get("actorid")})
                            elif ltag == "SetEffect":
                                inlive.append({"lcommande" : "setEffect",
                                    "param" : lcommand.get("param"),
                                    "param_1" : lcommand.get("param_1")})
                            elif ltag == "WaitEffect":
                                inlive.append({"lcommande" : "waitEffect"})
                            elif ltag == "SetAnimation":
                                inlive.append({"lcommande" : "setAnimation",
                                    "animid" : lcommand.get("animid")})
                            elif ltag == "SlidePositionMark":
                                inlive.append({"lcommande":"slidePositionMark",
                                    "param" : lcommand.get("param"),
                                    "param_1" : lcommand.get("param_1"),
                                    "param_2" : lcommand.get("param_2"),
                                    "param_3" : lcommand.get("param_3"),
                                    "param_4" : lcommand.get("param_4")})
                            elif ltag == "SetFunctionAttribute":
                                inlive.append({"lcommande" : "setFunctionAttribute",
                                    "param" : lcommand.get("param")})
                            elif ltag == "SetPositionMark":
                                inlive.append({"lcommande" : "setPositionMark",
                                    "param" : lcommand.get("param"),
                                    "param_1" : lcommand.get("param_1"),
                                    "param_2" : lcommand.get("param_2"),
                                    "param_3" : lcommand.get("param_3")})
                            elif ltag == "SetDirection":
                                inlive.append({"lcommande" : "setDirection",
                                    "direction" : lcommand.get("direction")})
                            elif ltag == "MovePositionOffset":
                                inlive.append({"lcommande" : "movePositionOffset",
                                    "param" : lcommand.get("param"),
                                    "x" : lcommand.get("x"),
                                    "y" : lcommand.get("y")})
                            elif ltag == "SetPositionInitial":
                                inlive.append({"lcommande" : "setPositionInitial"})
                            elif ltag == "WaitAnimation":
                                inlive.append({"lcommande" : "waitAnimation"})
                            elif ltag == "SlidePositionOffset":
                                inlive.append({"lcommande" : "slidePositionOffset",
                                    "param" : lcommand.get("param"),
                                    "x" : lcommand.get("x"),
                                    "y" : lcommand.get("y")})
                            elif ltag == "Move2PositionOffset":
                                inlive.append({"lcommande" : "move2PositionOffset",
                                    "param" : lcommand.get("param"),
                                    "x" : lcommand.get("x"),
                                    "y" : lcommand.get("y")})
                            elif ltag == "SetOutputAttribute":
                                inlive.append({"lcommande" : "setOutputAttribute",
                                    "param" : lcommand.get("param")})
                            elif ltag == "ResetHitAttribute":
                                inlive.append({"lcommande" : "resetHitAttribute",
                                    "param" : lcommand.get("param")})
                            elif ltag == "Turn2DirectionTurn":
                                inlive.append({"lcommande" : "turn2DirectionTurn",
                                    "param" : lcommand.get("param"),
                                    "param_1" : lcommand.get("param_1"),
                                    "param_2" : lcommand.get("param_2")})
                            elif ltag == "Slide2PositionOffset":
                                inlive.append({"lcommande" : "slide2PositionOffset",
                                    "param" : lcommand.get("param"),
                                    "x" : lcommand.get("x"),
                                    "y" : lcommand.get("y")})
                            elif ltag == "Destroy":
                                inlive.append({"lcommande" : "destroy"})
                            elif ltag == "ResetOutputAttribute":
                                inlive.append({"lcommande" : "resetOutputAttribute",
                                    "param" : lcommand.get("param")})
                            elif ltag == "MoveHeight":
                                inlive.append({"lcommande" : "moveHeight",
                                    "param" : lcommand.get("param"),
                                    "param_1" : lcommand.get("param_1")})
                            elif ltag == "SetPositionOffset":
                                inlive.append({"lcommande" : "setPositionOffset",
                                    "param" : lcommand.get("param"),
                                    "param_1" : lcommand.get("param_1")})
                            elif ltag == "ResetFunctionAttribute":
                                inlive.append({"lcommande" : "resetFunctionAttribute",
                                    "param" : lcommand.get("param")})
                            elif ltag == "MovePosition":
                                inlive.append({"lcommande" : "moveposition",
                                    "param" : lcommand.get("param"),
                                    "x" : lcommand.get("x"),
                                    "y" : lcommand.get("y")})
                            elif ltag == "Turn3":
                                inlive.append({"lcommande" : "turn3",
                                    "param" : lcommand.get("param"),
                                    "param_1" : lcommand.get("param_1"),
                                    "param_2" : lcommand.get("param_2"),
                                    "param_3" : lcommand.get("param_3")})
                            elif ltag == "Hold":
                                inlive.append({"lcommande" : "hold"})
                            elif ltag == "SetupOutputAttributeAndAnimation":
                                inlive.append({"lcommande" : "SetupOutputAttributeAndAnimation",
                                    "param" : lcommand.get("param"),
                                    "param_1" : lcommand.get("param_1"),
                                    "param_2" : lcommand.get("param_2")})
                            elif ltag == "PursueTurnLives":
                                inlive.append({"lcommande" : "pursueTurnLives",
                                    "param" : lcommand.get("param"),
                                    "param_1" : lcommand.get("param_1"),
                                    "param_2" : lcommand.get("param_2"),
                                    "param_3" : lcommand.get("param_3")})
                            elif ltag == "PursueTurnLives2":
                                inlive.append({"lcommande" : "pursueTurnLives2",
                                    "param" : lcommand.get("param"),
                                    "param_1" : lcommand.get("param_1"),
                                    "param_2" : lcommand.get("param_2"),
                                    "param_3" : lcommand.get("param_3")})
                            elif ltag == "EndAnimation":
                                inlive.append({"lcommande" : "endAnimation"})
                            elif ltag == "SetBlink":
                                inlive.append({"lcommande" : "setBlink",
                                    "param" : lcommand.get("param"),
                                    "param_1" : lcommand.get("param_1")})
                            else:
                                print("erreur : live inconnue : " + ltag)
                                inlive.append({"lcommande" : "inconnu"})
                        obj = {"commande" : "lives",
                               "actorid" : command.get("actorid"),
                               "in" : inlive}#TODO : in
                        funcl.append(obj)
                    elif tag == "WaitExecuteLives":
                        obj = {"commande" : "waitExecuteLives",
                               "actorid" : command.get("actorid")}
                        funcl.append(obj)
                    elif tag == "SwitchSector":
                        obj = {"commande" : "switchSector",
                               "in" : "TODO"}#TODO : in
                        funcl.append(obj)
                    elif tag == "End":
                        obj = {"commande" : "end"}
                        funcl.append(obj)
                    elif tag == "message_Talk":
                        caset = []
                        for lang in command:
                            caset.append([lang.get("language"),lang.text])
                        obj = {"commande" : "messageTalk",
                               "text" : caset}
                        funcl.append(obj)
                    elif tag == "message_Close":
                        obj = {"commande" : "messageClose"}
                        funcl.append(obj)
                    elif tag == "screen_FadeOut":
                        obj = {"commande" : "screenFadeOut",
                               "bool" : command.get("bool"),
                               "duration" : command.get("duration")}
                        funcl.append(obj)
                    elif tag == "message_SetActor":
                        obj = {"commande" : "messageSetActor",
                               "actorid" : command.get("actorid")}
                        funcl.append(obj)
                    elif tag == "object":
                        inobject = []
                        for ocommand in command:
                            otag = ocommand.tag
                            if otag == "SetOutputAttribute":
                                inobject.append({"ocommande" : "setOutputAttribute",
                                    "param" : ocommand.get("param")})
                            elif otag == "Move2PositionOffset":
                                inobject.append({"ocommande" : "move2PositionOffset",
                                    "param" : ocommand.get("param"),
                                    "x" : ocommand.get("x"),
                                    "y" : ocommand.get("y")})
                            elif otag == "MoveHeight":
                                inobject.append({"ocommande" : "moveHeight",
                                    "param" : ocommand.get("param"),
                                    "param_1" : ocommand.get("param_1")})
                            elif otag == "MovePositionOffset":
                                inobject.append({"ocommande" : "movePositionOffset",
                                    "param" : ocommand.get("param"),
                                    "x" : ocommand.get("x"),
                                    "y" : ocommand.get("y")})
                            elif otag == "MovePositionMark":
                                inobject.append({"ocommande" : "movePositionMark",
                                    "param" : ocommand.get("param"),
                                    "param_1" : ocommand.get("param_1"),
                                    "param_2" : ocommand.get("param_2"),
                                    "x" : ocommand.get("x"),
                                    "y" : ocommand.get("y")})
                            elif otag == "Destroy":
                                inobject.append({"ocommande":"destroy"})
                            elif otag == "SetAnimation":
                                inobject.append({"ocommande":"setAnimation",
                                    "animid" : ocommand.get("animid")})
                            elif otag == "SetPositionMark":
                                inobject.append({"ocommande" : "setPositionMark",
                                    "param" : ocommand.get("param"),
                                    "param_1" : ocommand.get("param_1"),
                                    "param_2" : ocommand.get("param_2"),
                                    "param_3" : ocommand.get("param_3")})
                            elif otag == "SetupOutputAttributeAndAnimation":
                                inobject.append({"ocommande" : "setupOutputAttributeAndAnimation",
                                    "param" : ocommand.get("param"),
                                    "param_1" : ocommand.get("param_1"),
                                    "param_2" : ocommand.get("param_2")})
                            elif otag == "WaitAnimation":
                                inobject.append({"ocommande" : "waitAnimation"})
                            elif otag == "SetHeight":
                                inobject.append({"ocommande" : "setHeight",
                                    "param" : ocommand.get("param")})
                            elif otag == "Move2PositionMark":
                                inobject.append({"ocommande":"move2PositionMark",
                                    "param":ocommand.get("param"),
                                    "param_1":ocommand.get("param_1"),
                                    "param_2":ocommand.get("param_2"),
                                    "param_3":ocommand.get("param_3"),
                                    "param_4":ocommand.get("param_4")})
                            elif otag == "Slide2PositionOffset":
                                inobject.append({"ocommande" : "slide2PositionOffset",
                                    "param" : ocommand.get("param"),
                                    "x" : ocommand.get("x"),
                                    "y" : ocommand.get("y")})
                            elif otag == "SetPositionLives":
                                inobject.append({"ocommande" : "setPositionLives",
                                    "param" : ocommand.get("param")})
                            elif otag == "SetPositionOffset":
                                inobject.append({"ocommande" : "setPositionOffset",
                                    "param" : ocommand.get("param"),
                                    "param_1" : ocommand.get("param_1")})
                            elif otag == "ResetOutputAttribute":
                                inobject.append({"ocommande" : "resetOutputAttribute",
                                    "param" : ocommand.get("param")})
                            else:
                                print("erreur : commande d'object inconnue : " + otag)
                                inobject.append({"ocommande" : "inconnu"})
                        obj = {"commande" : "object",
                               "objectid" : command.get("objectid"),
                               "in" : inobject}#TODO : in
                        funcl.append(obj)
                    elif tag == "se_Play":
                        obj = {"commande" : "sePlay",
                               "param" : command.get("param")}
                        funcl.append(obj)
                    elif tag == "screen2_FadeOut":
                        obj = {"commande" : "screen2FadeOut",
                               "bool" : command.get("bool"),
                               "duration" : command.get("duration")}
                        funcl.append(obj)
                    elif tag == "bgm_FadeOut":
                        obj = {"commande" : "bgmFadeOut",
                               "duration" : command.get("duration")}
                        funcl.append(obj)
                    elif tag == "WaitBgm":
                        obj = {"commande" : "waitBgm",
                               "bgm" : command.get("bgm")}
                        funcl.append(obj)
                    elif tag == "WaitSe":
                        obj = {"commande" : "waitSe",
                               "param" : command.get("param")}
                        funcl.append(obj)
                    elif tag == "camera_SetEffect":
                        obj = {"commande" : "cameraSetEffect",
                                "param" : command.get("param"),
                                "param_1" : command.get("param_1"),
                                "param_2" : command.get("param_2")}
                        funcl.append(obj)
                    elif tag == "WaitExecuteObject":
                        obj = {"commande" : "waitExecuteObject",
                               "objectid" : command.get("objectid")}
                        funcl.append(obj)
                    elif tag == "se_Stop":
                        obj = {"commande" : "seStop",
                               "param" : command.get("param")}
                        funcl.append(obj)
                    elif tag == "message_EmptyActor":
                        obj = {"commande" : "messageEmptyActor"}
                        funcl.append(obj)
                    elif tag == "WaitExecutePerformer":
                        obj = {"commande" : "waitExecutePerformer",
                               "performerid" : command.get("performerid")}
                        funcl.append(obj)
                    elif tag == "message_SwitchMonologue":
                        caseText = []
                        defaultText = None
                        for case in command:
                            caset = []
                            for lang in case:
                                caset.append([lang.get("language"),lang.text])
                            if case.tag == "CaseText":
                                caseText.append({"type" : case.keys()[0],
                                                 "value" : case.get(case.keys()[0]),
                                                 "text" : caset})
                            elif case.tag == "DefaultText":
                                defaultText = caset
                            else:
                                print("erreur non bloquante : type de condition de texte non definie.")
                        obj = {"commande" : "messageSwitchMonologue",
                               "svar" : command.get("svar"),
                               "case" : caseText,
                               "default" : defaultText}
                        funcl.append(obj)
                    elif tag == "message_ResetActor":
                        obj = {"commande" : "messageResetActor"}
                        funcl.append(obj)
                    elif tag == "flag_SetScenario":
                        obj = {"commande" : "flagSetScenario",
                               "svar" : command.get("svar"),
                               "param_1" : command.get("param_1"),
                               "param_2" : command.get("param_2")}
                        funcl.append(obj)
                    elif tag == "flag_SetDungeonMode":
                        obj = {"commande" : "flagSetDungeonMode",
                               "param" : command.get("param"),
                               "param_1" : command.get("param_1")}
                        funcl.append(obj)
                    elif tag == "back_SetBanner2":
                        caset = []
                        for lang in command:
                            caset.append([lang.get("language"),lang.text])
                        obj = {"commande" : "backSetBanner2",
                               "param" : command.get("param"),
                               "param_1" : command.get("param_1"),
                               "x" : command.get("x"),
                               "y" : command.get("y"),
                               "param_4" : command.get("param_4"),
                               "text" : caset}
                        funcl.append(obj)
                    elif tag == "screen_FlushIn":
                        obj = {"commande" : "screenFlushIn",
                               "param" : command.get("param"),
                               "param_1" : command.get("param_1"),
                               "param_2" : command.get("param_2"),
                               "param_3" : command.get("param_3"),
                               "param_4" : command.get("param_4"),
                               "param_5" : command.get("param_5")}
                        funcl.append(obj)
                    elif tag == "screen2_FlushIn":
                        obj = {"commande" : "screen2FlushIn",
                               "param" : command.get("param"),
                               "param_1" : command.get("param_1"),
                               "param_2" : command.get("param_2"),
                               "param_3" : command.get("param_3"),
                               "param_4" : command.get("param_4"),
                               "param_5" : command.get("param_5")}
                        funcl.append(obj)
                    elif tag == "screen_FlushOut":
                        obj = {"commande" : "screenFlushOut",
                               "param" : command.get("param"),
                               "param_1" : command.get("param_1"),
                               "param_2" : command.get("param_2"),
                               "param_3" : command.get("param_3"),
                               "param_4" : command.get("param_4"),
                               "param_5" : command.get("param_5")}
                        funcl.append(obj)
                    elif tag == "screen2_FlushOut":
                        obj = {"commande" : "screen2FlushOut",
                               "param" : command.get("param"),
                               "param_1" : command.get("param_1"),
                               "param_2" : command.get("param_2"),
                               "param_3" : command.get("param_3"),
                               "param_4" : command.get("param_4"),
                               "param_5" : command.get("param_5")}
                        funcl.append(obj)
                    elif tag == "camera2_SetPositionMark":
                        obj = {"commande" : "camera2SetPositionMark",
                               "param" : command.get("param"),
                               "param_1" : command.get("param_1"),
                               "param_2" : command.get("param_2"),
                               "param_3" : command.get("param_3")}
                        funcl.append(obj)
                    elif tag == "camera_SetPositionMark":
                        obj = {"commande" : "cameraSetPositionMark",
                               "param" : command.get("param"),
                               "param_1" : command.get("param_1"),
                               "param_2" : command.get("param_2"),
                               "param_3" : command.get("param_3")}
                        funcl.append(obj)
                    elif tag == "supervision_RemoveActing":
                        obj = {"commande" : "supervisionRemoveActing",
                               "layerid" : command.get("layerid")}
                        funcl.append(obj)
                    elif tag == "message_SetFaceOnly":
                        obj = {"commande" : "messageSetFaceOnly",
                               "actorid" : command.get("actorid"),
                               "face" : command.get("face"),
                               "param_2" : command.get("param_2")}
                        funcl.append(obj)
                    elif tag == "WaitScreenFadeAll":
                        obj = {"commande" : "waitScreenFadeAll"}
                        funcl.append(obj)
                    elif tag == "WaitScreenFade":
                        obj = {"commande" : "waitScreenFade"}
                        funcl.append(obj)
                    elif tag == "SetAnimation":
                        obj = {"commande" : "setAnimation",
                               "animid" : command.get("animid")}
                        funcl.append(obj)
                    elif tag == "screen_FadeOutAll":
                        obj = {"commande" : "screenFadeOutAll",
                               "bool" : command.get("bool"),
                               "duration" : command.get("duration")}
                        funcl.append(obj)
                    elif tag == "Label":
                        obj = {"commande" : "label",
                               "id" : command.get("id")}
                        funcl.append(obj)
                    elif tag == "JumpCommon":
                        obj = {"commande" : "jumpCommon",
                               "croutineid" : command.get("croutineid")}
                        funcl.append(obj)
                    elif tag == "debug_Print":
                        obj = {"commande" : "debugPrint",
                               "constref" : command.get("constref")}
                        funcl.append(obj)
                    elif tag == "Jump":
                        obj = {"commande" : "jump",
                                "tolabel" : command.get("tolabel")}
                        funcl.append(obj)
                    elif tag == "Switch":
                        obj = {"commande" : "switch",
                               "svar" : command.get("svar")}
                        funcl.append(obj)
                        #print(obj)
                    elif tag == "message_Notice":
                        caset = []
                        for lang in command:
                            caset.append([lang.get("language"),lang.text])
                        obj = {"commande" : "messageNotice",
                               "text" : caset}
                        funcl.append(obj)
                    elif tag == "supervision_ExecuteStation":
                        obj = {"commande" : "supervisionExecuteStation",
                               "levelid" : command.get("levelid"),
                               "constref" : command.get("constref"),
                               "param_2" : command.get("param_2")}
                        funcl.append(obj)
                    elif tag == "Hold":
                        obj = {"commande" : "hold"}
                        funcl.append(obj)
                    elif tag == "BranchBit":
                        obj = {"commande" : "branchBit",
                               "svar" : command.get("svar"),
                               "param_1" : command.get("param_1"),
                               "tolabel" : command.get("tolabel")}
                        funcl.append(obj)
                    elif tag == "BranchScenarioBefore":
                        obj = {"commande" : "branchScenarioBefore",
                               "svar" : command.get("svar"),
                               "param_1" : command.get("param_1"),
                               "param_2" : command.get("param_2"),
                               "tolabel" : command.get("tolabel")}
                        funcl.append(obj)
                    elif tag == "BranchScenarioNow":
                        obj = {"commande" : "BranchScenarioNow",
                               "svar" : command.get("svar"),
                               "param_1" : command.get("param_1"),
                               "param_2" : command.get("param_2"),
                               "tolabel" : command.get("tolabel")}
                        funcl.append(obj)
                    elif tag == "ProcessSpecial":
                        obj = {"commande" : "processSpecial",
                               "procspec" : command.get("procspec"),
                               "param_1" : command.get("param_1"),
                               "param_2" : command.get("param_2")}
                        funcl.append(obj)
                    elif tag == "supervision_ExecuteStationSub":
                        obj = {"commande" : "supervisionExecuteStationSub",
                               "levelid" : command.get("levelid"),
                               "constref" : command.get("constref"),
                               "param_2" : command.get("param_2")}
                        funcl.append(obj)
                    elif tag == "SwitchScenario":
                        obj = {"commande" : "switchScenario",
                               "svar" : command.get("svar"),
                               "in" : "TODO"} #TODO : in
                        funcl.append(obj)
                    elif tag == "BranchScenarioNowAfter":
                        obj = {"commande" : "BranchScenarioNowAfter",
                               "svar" : command.get("svar"),
                               "param_1" : command.get("param_1"),
                               "param_2" : command.get("param_2"),
                               "tolabel" : command.get("tolabel")}
                        funcl.append(obj)
                    elif tag == "WaitSubScreen":
                        obj = {"commande" : "waitSubScreen"}
                        funcl.append(obj)
                    elif tag == "WaitFadeIn":
                        obj = {"commande" : "waitFadeIn"}
                        funcl.append(obj)
                    elif tag == "message_Monologue":
                        caset = []
                        for lang in command:
                            caset.append([lang.get("language"),lang.text])
                        obj = {"commande" : "messageMonologue",
                               "text" : caset}
                        funcl.append(obj)
                    elif tag == "screen_FadeChange":
                        obj = {"commande" : "screenFadeChange",
                               "param" : command.get("param"),
                               "param_1" : command.get("param_1"),
                               "param_2" : command.get("param_2"),
                               "param_3" : command.get("param_3")}
                        funcl.append(obj)
                    elif tag == "bgm_ChangeVolume":
                        obj = {"commande" : "bgmChangeVolume",
                               "duration" : command.get("duration"),
                               "vol" : command.get("vol")}
                        funcl.append(obj)
                    elif tag == "bgm2_PlayFadeIn":
                        obj = {"commande" : "bgm2PlayFadeIn",
                               "bgm" : command.get("bgm"),
                               "duration" : command.get("duration"),
                               "vol" : command.get("vol")}
                        funcl.append(obj)
                    elif tag == "message_Mail":
                        caset = []
                        for lang in command:
                            caset.append([lang.get("language"),lang.text])
                        obj = {"commande" : "messageMail",
                               "text" : caset}
                        funcl.append(obj)
                    elif tag == "bgm2_FadeOut":
                        obj = {"commande" : "bgm2FadeOut",
                               "param" : command.get("param")}
                        funcl.append(obj)
                    elif tag == "WaitBgm2":
                        obj = {"commande" : "waitBgm2",
                               "param" : command.get("param")}
                        funcl.append(obj)
                    elif tag == "message_KeyWait":
                        obj = {"commande" : "messageKeyWait"}
                        funcl.append(obj)
                    elif tag == "back2_SetEffect":
                        obj = {"commande" : "back2SetEffect",
                               "param" : command.get("param"),
                               "param_1" : command.get("param_1")}
                        funcl.append(obj)
                    elif tag == "flag_CalcBit":
                        obj = {"commande" : "flagCalcBit",
                               "svar" : command.get("svar"),
                               "param_1" : command.get("param_1"),
                               "param_2" : command.get("param_2")}
                        funcl.append(obj)
                    elif tag == "me_Play":
                        obj = {"commande" : "mePlay",
                               "param" : command.get("param")}
                        funcl.append(obj)
                    elif tag == "message_Explanation":
                        caset = []
                        for lang in command:
                            temp51 = [lang.get("language"),lang.text]
                            if type(temp51[1]) != str:
                                temp51[1] = ""
                            caset.append(temp51)
                        obj = {"commande" : "messageExplanation",
                               "text" : caset}
                        funcl.append(obj)
                    elif tag == "flag_Set":
                        obj = {"commande" : "flagSet",
                               "to" : command.get("int"),
                               "type" : "int"} #TODO : check int cant be str
                        funcl.append(obj)
                    elif tag == "message_SwitchMenu":
                        lcase = []
                        for loop in command:
                            if loop.tag == "CaseMenu":
                                langl = []
                                for loop2 in loop:
                                    langl.append([loop2.get("language"),loop2.text])
                                lcase.append(["normal",loop.get("tolabel"),langl])
                            elif loop.tag == "CaseMenu2":
                                lcase.append("ex")#TODO
                        obj = {"commande" : "messageSwitchMenu",
                               "param" : command.get("param"),
                               "param_1" : command.get("param_1"),
                               "lcase" : lcase}
                        funcl.append(obj)
                    elif tag == "back_SetBackEffect":
                        obj = {"commande" : "backSetBackEffect",
                               "param" : command.get("param")}
                        funcl.append(obj)
                    elif tag == "screen_WhiteOut":
                        obj = {"commande" : "screenWhiteOut",
                               "bool" : command.get("bool"),
                               "duration" : command.get("duration")}
                        funcl.append(obj)
                    elif tag == "message_CloseEnforce":
                        obj = {"commande" : "messageCloseEnforce"}
                        funcl.append(obj)
                    elif tag == "message_Narration":
                        caset = []
                        for lang in command:
                            caset.append([lang.get("language"),lang.text])
                        obj = {"commande" : "messageNarration",
                               "param" : command.get("param"),
                               "text" : caset}
                        funcl.append(obj)
                    elif tag == "supervision_LoadStation":
                        obj = {"commande" : "supervisionLoadStation",
                               "levelid" : command.get("levelid"),
                               "constref" : command.get("constref")}
                        funcl.append(obj)
                    elif tag == "supervision_Station":
                        obj = {"commande" : "supervisionStation",
                               "stationid" : command.get("stationid")}
                        funcl.append(obj)
                    elif tag == "supervision_SpecialActing":
                        obj = {"commande" : "supervisionSpecialActing",
                               "param" : command.get("param"),
                               "param_1" : command.get("param_1"),
                               "param_2" : command.get("param_2")}
                        funcl.append(obj)
                    elif tag == "supervision2_SpecialActing":
                        obj = {"commande" : "supervision2SpecialActing",
                               "param" : command.get("param"),
                               "param_1" : command.get("param_1"),
                               "param_2" : command.get("param_2")}
                        funcl.append(obj)
                    elif tag == "message_Menu":
                        obj = {"commande" : "messageMenu",
                               "menuid" : command.get("menuid")}
                        funcl.append(obj)
                    elif tag == "bgm2_Stop":
                        obj = {"commande" : "bgm2Stop"}
                        funcl.append(obj)
                    elif tag == "message_FacePositionOffset":
                        obj = {"commande" : "messageFacePositionOffset",
                               "x" : command.get("x"),
                               "y" : command.get("y")}
                        funcl.append(obj)
                    elif tag == "main_EnterDungeon":
                        obj = {"commande" : "mainEnterDungeon",
                               "param" : command.get("param"),
                               "param_1" : command.get("param_1")}
                        funcl.append(obj)
                    elif tag == "WaitLockLives":
                        obj = {"commande" : "waitLockLives",
                               "param" : command.get("param"),
                               "param_1" : command.get("param_1")}
                        funcl.append(obj)
                    elif tag == "Unlock":
                        obj = {"commande" : "unlock",
                               "param" : command.get("param")}
                        funcl.append(obj)
                    elif tag == "Lock":
                        obj = {"commande" : "lock",
                               "param" : command.get("param")}
                        funcl.append(obj)
                    elif tag == "SetDirection":
                        obj = {"commande" : "setDirection",
                               "direction" : command.get("direction")}
                        funcl.append(obj)
                    elif tag == "back2_SetBackEffect":
                        obj = {"commande" : "back2SetBackEffect",
                               "param" : command.get("param")}
                        funcl.append(obj)
                    elif tag == "screen2_WhiteOut":
                        obj = {"commande" : "screen2WhiteOut",
                               "bool" : command.get("bool"),
                               "duration" : command.get("duration")}
                        funcl.append(obj)
                    elif tag == "flag_Clear":
                        obj = {"commande" : "flagClear",
                               "svar" : command.get("svar")}
                        funcl.append(obj)
                    elif tag == "bgm2_ChangeVolume":
                        obj = {"commande" : "bgm2ChangeVolume",
                               "param" : command.get("param"),
                               "param_1" : command.get("param_1")}
                        funcl.append(obj)
                    elif tag == "flag_CalcValue":
                        obj = {"commande" : "flagCalcValue",
                               "svar" : command.get("svar"),
                               "param_1" : command.get("param_1"),
                               "int" : command.get("int")}
                        funcl.append(obj)
                    elif tag == "message_SetWaitMode":
                        obj = {"commande" : "messageSetWaitMode",
                               "param" : command.get("param"),
                               "param_1" : command.get("param_1")}
                        funcl.append(obj)
                    elif tag == "SetOutputAttribute":
                        obj = {"commande" : "setOutputAttribute",
                               "param" : command.get("param")}
                        funcl.append(obj)
                    elif tag == "SlidePositionOffset":
                        obj = {"commande" : "slidePositionOffset",
                               "param" : command.get("param"),
                               "x" : command.get("x"),
                               "y" : command.get("y")}
                        funcl.append(obj)
                    elif tag == "SetEffect":
                        obj = {"commande" : "setEffect",
                               "param" : command.get("param"),
                               "param_1" : command.get("param_1")}
                        funcl.append(obj)
                    elif tag == "WaitAnimation":
                        obj = {"commande" : "waitAnimation"}
                        funcl.append(obj)
                    elif tag == "Turn2Direction":
                        obj = {"commande" : "turn2Direction",
                               "param" : command.get("param"),
                               "param_1" : command.get("param_1"),
                               "direction" : command.get("direction")}
                        funcl.append(obj)
                    elif tag == "WaitBgmSignal":
                        obj = {"commande" : "waitBgmSignal"}
                        funcl.append(obj)
                    elif tag == "WaitEffect":
                        obj = {"commande" : "waitEffect"}
                        funcl.append(obj)
                    elif tag == "SetPositionOffset":
                        obj = {"commande" : "setPositionOffset",
                               "param" : command.get("param"),
                               "param_1" : command.get("param_1")}
                        funcl.append(obj)
                    elif tag == "back_SetDungeonBanner":
                        obj = {"commande" : "backSetDungeonBanner",
                               "param" : command.get("param"),
                               "param_1" : command.get("param_1")}
                        funcl.append(obj)
                    elif tag == "bgm_Stop":
                        obj = {"commande" : "bgmStop"}
                        funcl.append(obj)
                    elif tag == "BranchPerformance":
                        obj = {"commande" : "branchPerformance",
                               "param" : command.get("param"),
                               "param_1" : command.get("param_1"),
                               "param_2" : command.get("param_2")}
                        funcl.append(obj)
                    elif tag == "BranchVariation":
                        obj = {"commande" : "branchVariation",
                               "svar" : command.get("svar"),
                               "tolabel" : command.get("tolabel")}
                        funcl.append(obj)
                    elif tag == "SwitchScenarioLevel":
                        obj = {"commande" : "switchScenarioLevel",
                               "svar" : command.get("svar"),
                               "in" : "TODO"} #TODO : in
                        funcl.append(obj)
                    elif tag == "MovePositionMark":
                        obj = {"commande" : "movePositionMark",
                               "param" : command.get("param"),
                               "param_1" : command.get("param_1"),
                               "param_2" : command.get("param_2"),
                               "x" : command.get("x"),
                               "y" : command.get("y")}
                        funcl.append(obj)
                    elif tag == "screen_WhiteOutAll":
                        obj = {"commande" : "screenWhiteOutAll",
                               "param" : command.get("param"),
                               "param_1" : command.get("param_1")}
                        funcl.append(obj)
                    elif tag == "screen_FadeInAll":
                        obj = {"commande" : "screenFadeInAll",
                               "bool" : command.get("bool"),
                               "duration" : command.get("duration")}
                        funcl.append(obj)
                    elif tag == "se_FadeOut":
                        obj = {"commande" : "seFadeOut",
                               "param" : command.get("param"),
                               "param_1" : command.get("param_1")}
                        funcl.append(obj)
                    elif tag == "SetPositionInitial":
                        obj = {"commande" : "setPositionInitial"}
                        funcl.append(obj)
                    elif tag == "supervision_ExecuteCommon":
                        obj = {"commande" : "supervisionExecuteCommon",
                               "croutineid" : command.get("croutineid")}
                        funcl.append(obj)
                    elif tag == "Branch":
                        obj = {"commande" : "branch",
                               "svar" : command.get("svar"),
                               "param_1" : command.get("param_1"),
                               "tolabel" : command.get("tolabel")}
                        funcl.append(obj)
                    elif tag == "camera_Move2Default":
                        obj = {"commande" : "cameraMove2Default",
                               "param" : command.get("param")}
                        funcl.append(obj)
                    elif tag == "supervision_Suspend":
                        obj = {"commande" : "supervisionSuspend",
                               "param" : command.get("param")}
                        funcl.append(obj)
                    elif tag == "message_ImitationSound":
                        caset = []
                        for lang in command:
                            caset.append([lang.get("language"),lang.text])
                        obj = {"commande" : "messageImitationSound",
                               "text" : caset}
                        funcl.append(obj)
                    elif tag == "WaitMe":
                        obj = {"commande" : "waitMe",
                               "param" : command.get("param")}
                        funcl.append(obj)
                    elif tag == "worldmap_SetMode":
                        obj = {"commande" : "worldmapSetMode",
                               "param" : command.get("param")}
                        funcl.append(obj)
                    elif tag == "worldmap_SetLevel":
                        obj = {"commande" : "worldmapSetLevel",
                               "param" : command.get("param")}
                        funcl.append(obj)
                    elif tag == "worldmap_ChangeLevel":
                        obj = {"commande" : "worldmapChangeLevel",
                               "param" : command.get("param")}
                        funcl.append(obj)
                    elif tag == "worldmap_SetCamera":
                        obj = {"commande" : "worldmapSetCamera",
                               "param" : command.get("param")}
                        funcl.append(obj)
                    elif tag == "ResetFunctionAttribute":
                        obj = {"commande" : "resetFunctionAttribute",
                               "param" : command.get("param")}
                        funcl.append(obj)
                    elif tag == "SlidePositionMark":
                        obj = {"commande" : "slidePositionMark",
                               "param" : command.get("param"),
                               "param_1" : command.get("param_1"),
                               "param_2" : command.get("param_2"),
                               "param_3" : command.get("param_3"),
                               "param_4" : command.get("param_4")}
                        funcl.append(obj)
                    elif tag == "SetFunctionAttribute":
                        obj = {"commande" : "setFunctionAttribute",
                               "param" : command.get("param")}
                        funcl.append(obj)
                    elif tag == "SlideHeight":
                        obj = {"commande" : "slideHeight",
                               "param" : command.get("param"),
                               "param_1" : command.get("param_1")}
                        funcl.append(obj)
                    elif tag == "main_SetGround":
                        obj = {"commande" : "mainSetGround",
                               "levelid" : command.get("levelid")}
                        funcl.append(obj)
                    elif tag == "main_EnterGround":
                        obj = {"commande" : "mainEnterGround",
                               "levelid" : command.get("levelid"),
                               "param_1" : command.get("param_1")}
                        funcl.append(obj)
                    elif tag == "supervision_RemoveCommon":
                        obj = {"commande" : "supervisionRemoveCommon",
                               "param" : command.get("param")}
                        funcl.append(obj)
                    elif tag == "Slide2PositionMark":
                        obj = {"commande" : "slide2PositionMark",
                               "param" : command.get("param"),
                               "param_1" : command.get("param_1"),
                               "param_2" : command.get("param_2"),
                               "param_3" : command.get("param_3"),
                               "param_4" : command.get("param_4")}
                        funcl.append(obj)
                    elif tag == "flag_SetPerformance":
                        obj = {"commande" : "flagSetPerformance",
                               "param" : command.get("param"),
                               "param_1" : command.get("param_1")}
                        funcl.append(obj)
                    elif tag == "MoveHeight":
                        obj = {"commande" : "moveHeight",
                               "param" : command.get("param"),
                               "param_1" : command.get("param")}
                        funcl.append(obj)
                    elif tag == "BranchDebug":
                        obj = {"commande" : "branchDebug",
                               "bool" : command.get("bool"),
                               "tolabel" : command.get("tolabel")}
                        funcl.append(obj)
                    elif tag == "WaitScreen2Fade":
                        obj = {"commande" : "waitScreen2Fade"}
                        funcl.append(obj)
                    elif tag == "screen_WhiteChange":
                        obj = {"commande" : "screenWhiteChange",
                               "param" : command.get("param"),
                               "param_1" : command.get("param_1"),
                               "param_2" : command.get("param_2"),
                               "param_3" : command.get("param_3")}
                        funcl.append(obj)
                    elif tag == "message_SetFaceEmpty":
                        obj = {"commande" : "messageSetFaceEmpty",
                               "param" : command.get("param"),
                               "param_1" : command.get("param_1"),
                               "param_2" : command.get("param_2")}
                        funcl.append(obj)
                    elif tag == "worldmap_SetArrow":
                        obj = {"commande" : "worldmapSetArrow",
                               "param" : command.get("param")}
                        funcl.append(obj)
                    elif tag == "worldmap_BlinkMark":
                        obj = {"commande" : "worldmapBlinkMark",
                               "param" : command.get("param")}
                        funcl.append(obj)
                    elif tag == "SwitchRandom":
                        obj = {"commande" : "switchRandom",
                               "param" : command.get("param"),
                               "in" : "TODO"}#TODO : in
                        funcl.append(obj)
                    elif tag == "supervision_ExecuteStationCommon":
                        obj = {"commande" : "supervisionExecuteStationCommon",
                               "levelid" : command.get("levelid"),
                               "param_1" : command.get("param_1")}
                        funcl.append(obj)
                    elif tag == "SetMoveRange":
                        obj = {"commande" : "setMoveRange",
                               "param" : command.get("param"),
                               "param_1" : command.get("param_1"),
                               "param_2" : command.get("param_2"),
                               "param_3" : command.get("param_3"),
                               "param_4" : command.get("param_4"),
                               "param_5" : command.get("param_5")}
                        funcl.append(obj)
                    elif tag == "se_PlayVolume":
                        obj = {"commande" : "sePlayVolume",
                               "param" : command.get("param"),
                               "param_1" : command.get("param_1")}
                        funcl.append(obj)
                    elif tag == "se_ChangeVolume":
                        obj = {"commande" : "seChangeVolume",
                               "param" : command.get("param"),
                               "param_1" : command.get("param_1"),
                               "param_2" : command.get("param_2")}
                        funcl.append(obj)
                    elif tag == "WaitRandom":
                        obj = {"commande" : "waitRandom",
                               "param" : command.get("param"),
                               "param_1" : command.get("param_1")}
                        funcl.append(obj)
                    elif tag == "MovePositionOffset":
                        obj = {"commande" : "movePositionOffset",
                               "param" : command.get("param"),
                               "x" : command.get("x"),
                               "y" : command.get("y")}
                        funcl.append(obj)#TODO : condition
                    elif tag == "camera2_SetEffect":
                        obj = {"commande" : "camera2SetEffect",
                               "param" : command.get("param"),
                               "param_1" : command.get("param_1"),
                               "param_2" : command.get("param_2")}
                        funcl.append(obj)
                    elif tag == "Slide2PositionLives":
                        obj = {"commande" : "slide2PositionLives",
                               "param" : command.get("param"),
                               "param_1" : command.get("param_1")}
                        funcl.append(obj)
                    elif tag == "supervision_ActingInvisible":
                        obj = {"commande" : "supervisionActingInvisible",
                               "layerid" : command.get("layerid")}
                        funcl.append(obj)
                    elif tag == "ResetOutputAttribute":
                        obj = {"commande" : "resetOutputAttribute",
                               "param" : command.get("param")}
                        funcl.append(obj)
                    elif tag == "back_SetEffect":
                        obj = {"commande" : "backSetEffect",
                               "param" : command.get("param"),
                               "param_1" : command.get("param_1")}
                        funcl.append(obj)
                    elif tag == "WaitBackEffect":
                        obj = {"commande" : "waitBackEffect"}
                        funcl.append(obj)
                    elif tag == "WaitEndAnimation":
                        obj = {"commande" : "waitEndAnimation"}
                        funcl.append(obj)
                    elif tag == "Turn2DirectionLives":
                        obj = {"commande" : "turn2DirectionLives",
                               "param" : command.get("param"),
                               "param_1" : command.get("param_1"),
                               "actorid" : command.get("actorid")}
                        funcl.append(obj)
                    elif tag == "Move2PositionLives":
                        obj = {"commande" : "move2PositionLives",
                               "param" : command.get("param"),
                               "param_1" : command.get("param_1")}
                        funcl.append(obj)
                    elif tag == "camera_SetDefault":
                        obj = {"commande" : "cameraSetDefault"}
                        funcl.append(obj)
                    elif tag == "Destroy":
                        obj = {"commande" : "destroy"}
                        funcl.append(obj)
                    elif tag == "StopAnimation":
                        obj = {"commande" : "stopAnimation"}
                        funcl.append(obj)
                    elif tag == "item_Set":
                        obj = {"commande" : "itemSet",
                               "param" : command.get("param"),
                               "itemid" : command.get("itemid"),
                               "param_2" : command.get("param_2")}
                        funcl.append(obj)
                    elif tag == "BranchScenarioNowBefore":
                        obj = {"commande" : "branchScenarioNowBefore",
                               "svar" : command.get("svar"),
                               "param_1" : command.get("param_1"),
                               "param_2" : command.get("param_2"),
                               "tolabel" : command.get("tolabel")}
                        funcl.append(obj)
                    elif tag == "item_SetTableData":
                        obj = {"commande" : "itemSetTableData",
                               "param" : command.get("param"),
                               "param_1" : command.get("param_1")}
                        funcl.append(obj)
                    elif tag == "back_SetWeather":
                        obj = {"commande" : "backSetWeather",
                               "param" : command.get("param")}
                        funcl.append(obj)
                    elif tag == "PauseEffect":
                        obj = {"commande" : "pauseEffect",
                               "param" : command.get("param")}
                        funcl.append(obj)
                    elif tag == "supervision_ExecuteActing":
                        obj = {"commande" : "supervisionExecuteActing",
                               "levelid" : command.get("levelid"),
                               "constref" : command.get("constref"),
                               "param_2" : command.get("param_2")}
                        funcl.append(obj)
                    elif tag == "bgm2_Play":
                        obj = {"commande" : "bgm2Play",
                             "bgm" : command.get("bgm")}
                        funcl.append(obj)
                    elif tag == "ResetHitAttribute":
                        obj = {"commande" : "resetHitAttribute",
                               "param" : command.get("param")}
                        funcl.append(obj)
                    elif tag == "back_ChangeGround":
                        obj = {"commande" : "backChangeGround",
                               "levelid" : command.get("levelid")}
                        funcl.append(obj)
                    elif tag == "camera_SetMyPosition":
                        obj = {"commande" : "cameraSetMyPosition"}
                        funcl.append(obj)
                    elif tag == "worldmap_SetMark":
                        obj = {"commande" : "worldmapSetMark",
                               "param" : command.get("param")}
                        funcl.append(obj)
                    elif tag == "worldmap_MoveCamera":
                        obj = {"commande" : "worldmapMoveCamera",
                               "param" : command.get("param")}
                        funcl.append(obj)
                    elif tag == "worldmap_SetMessagePlace":
                        obj = {"commande" : "worldmapSetMessagePlace",
                               "param" : command.get("param")}
                        funcl.append(obj)
                    elif tag == "main_EnterAdventure":
                        obj = {"commande" : "mainEnterAdventure",
                               "param" : command.get("param"),
                               "param_1" : command.get("param_1")}
                        funcl.append(obj)
                    elif tag == "camera_MoveDefault":
                        obj = {"commande" : "cameraMoveDefault",
                               "param" : command.get("param")}
                        funcl.append(obj)
                    elif tag == "screen2_WhiteChange":
                        obj = {"commande" : "screen2WhiteChange",
                               "param" : command.get("param"),
                               "param_1" : command.get("param_1"),
                               "param_2" : command.get("param_2"),
                               "param_3" : command.get("param_3")}
                        funcl.append(obj)
                    elif tag == "back_SetBackScrollSpeed":
                        obj = {"commande" : "backSetBackScrollSpeed",
                               "param" : command.get("param"),
                               "param_1" : command.get("param_1")}
                        funcl.append(obj)
                    elif tag == "Move2PositionMark":
                        obj = {"commande" : "move2PositionMark",
                               "param" : command.get("param"),
                               "param_1" : command.get("param_1"),
                               "param_2" : command.get("param_2"),
                               "param_3" : command.get("param_3"),
                               "param_4" : command.get("param_4")}
                        funcl.append(obj)
                    elif tag == "SetPositionMark":
                        obj = {"commande" : "setPositionMark",
                               "param" : command.get("param"),
                               "param_1" : command.get("param_1"),
                               "param_2" : command.get("param_2"),
                               "param_3" : command.get("param_3")}
                        funcl.append(obj)
                    elif tag == "back2_SetBackScrollSpeed":
                        obj = {"commande" : "back2SetBackScrollSpeed",
                               "param" : command.get("param"),
                               "param_1" : command.get("param_1")}
                        funcl.append(obj)
                    elif tag == "WaitLockObject":
                        obj = {"commande" : "waitLockObject",
                               "param" : command.get("param"),
                               "param_1" : command.get("param_1")}
                        funcl.append(obj)
                    elif tag == "Turn3":
                        obj = {"commande" : "turn3",
                               "param" : command.get("param"),
                               "param_1" : command.get("param_1"),
                               "param_2" : command.get("param_2"),
                               "param_3" : command.get("param_3")}
                        funcl.append(obj)
                    elif tag == "camera2_MovePositionMark":
                        obj = {"commande" : "camera2MovePositionMark",
                               "param" : command.get("param"),
                               "param_1" : command.get("param_1"),
                               "param_2" : command.get("param_2"),
                               "param_3" : command.get("param_3"),
                               "param_4" : command.get("param_4")}
                        funcl.append(obj)
                    elif tag == "WaitMoveCamera2":
                        obj = {"commande" : "waitMoveCamera2"}
                        funcl.append(obj)
                    elif tag == "worldmap_DeleteArrow":
                        obj = {"commande":"worldmapDeleteArrow"}
                        funcl.append(obj)
                    elif tag == "WaitMoveCamera":
                        obj = {"commande" : "waitMoveCamera"}
                        funcl.append(obj)
                    elif tag == "flag_SetAdventureLog":
                        obj = {"commande" : "flagSetAdventureLog",
                            "param" : command.get("param")}
                        funcl.append(obj)
                    elif tag == "item_GetVariable":
                        obj = {"commande" : "itemGetVariable",
                            "param" : command.get("param"),
                            "param_1" : command.get("param_1")}
                        funcl.append(obj)
                    elif tag == "back_SetSpecialEpisodeBanner3":
                        caset = []
                        for lang in command:
                            caset.append([lang.get("language"),lang.text])
                        obj = {"commande" : "backSetSpecialEpisodeBanner3",
                               "text" : caset}
                        funcl.append(obj)
                    elif tag == "back_SetSpecialEpisodeBanner":
                        caset = []
                        for lang in command:
                            caset.append([lang.get("language"),lang.text])
                        obj = {"commande" : "backSetSpecialEpisodeBanner",
                               "text" : caset}
                        funcl.append(obj)
                    elif tag == "back_SetSpecialEpisodeBanner2":
                        caset = []
                        for lang in command:
                            caset.append([lang.get("language"),lang.text])
                        obj = {"commande" : "backSetSpecialEpisodeBanner2",
                               "text" : caset}
                        funcl.append(obj)
                    elif tag == "back_SetBackScrollOffset":
                        obj = {"commande" : "backSetBackScrollOffset",
                            "param" : command.get("param"),
                            "param_1" : command.get("param")}
                    elif tag == "camera_SetMyself":
                        obj = {"commande" : "cameraSetMyself"}
                        funcl.append(obj)
                    elif tag == "camera_Move2PositionMark":
                        obj = {"commande" : "cameraMove2PositionMark",
                            "param" : command.get("param"),
                            "param_1" : command.get("param_1"),
                            "param_2" : command.get("param_2"),
                            "param_3" : command.get("param_3"),
                            "param_4" : command.get("param_4"),
                            "param_5" : command.get("param_5"),
                            "param_6" : command.get("param_6"),
                            "param_7" : command.get("param_7"),
                            "param_8" : command.get("param_8"),
                            "param_9" : command.get("param_9"),
                            "param_10" : command.get("param_10"),
                            "param_11" : command.get("param_11"),
                            "param_12" : command.get("param_12"),
                            "param_13" : command.get("param_13"),
                            "param_14" : command.get("param_14"),
                            "param_15" : command.get("param_15"),
                            "param_16" : command.get("param_16")}
                        funcl.append(obj)
                    elif tag=="Slide2PositionOffset":
                        obj = {"commande" : "slide2PositionOffset",
                            "param" : command.get("param"),
                            "x" : command.get("x"),
                            "y" : command.get("y")}
                        funcl.append(obj)
                    elif tag=="Move3PositionOffset":
                        obj = {"commande" : "move3PositionOffset",
                            "param" : command.get("param"),
                            "x" : command.get("x"),
                            "y" : command.get("y")}
                        funcl.append(obj)
                    elif tag=="MoveDirection":
                        obj = {"commande" : "moveDirection",
                            "param" : command.get("param"),
                            "param_1" : command.get("param_1"),
                            "param_2" : command.get("param_2")}
                        funcl.append(obj)
                    elif tag=="MoveTurn":
                        obj = {"commande" : "moveTurn",
                            "param" : command.get("param"),
                            "param_1" : command.get("param_1"),
                            "param_2" : command.get("param_2")}
                        funcl.append(obj)
                    elif tag=="Turn2DirectionLives2":
                        obj = {"commande" : "turn2directionLives2",
                            "param" : command.get("param"),
                            "param_1" : command.get("param_1"),
                            "param_2" : command.get("param_2")}
                        funcl.append(obj)
                    elif tag=="WaitLockSupervision":
                        obj = {"commande" : "waitLockSupervision",
                            "param" : command.get("param")}
                        funcl.append(obj)
                    elif tag=="MoveSpecial":
                        obj = {"commande" : "moveSpecial",
                            "param" : command.get("param"),
                            "param_1" : command.get("param_1"),
                            "param_2" : command.get("param_2")}
                        funcl.append(obj)
                    elif tag == "Call":
                        obj = {"commande" : "call",
                            "lroutineid" : command.get("lroutineid")}
                        funcl.append(obj)
                    elif tag == "Return":
                        obj = {"commande" : "return"}
                        funcl.append(obj)
                    elif tag=="Slide3PositionOffset":
                        obj = {"commande" : "slide3PositionOffset",
                            "param" : command.get("param"),
                            "x" : command.get("x"),
                            "y" : command.get("y")}
                        funcl.append(obj)
                    elif tag=="back2_SetWeather":
                        obj = {"commande" : "back2SetWeather",
                            "param" : command.get("param")}
                        funcl.append(obj)
                    elif tag == "back_SetBanner":
                        caset = []
                        for lang in command:
                            caset.append([lang.get("language"),lang.text])
                        obj = {"commande" : "backSetBanner",
                               "param" : command.get("param")}
                        funcl.append(obj)
                    elif tag == "back_SetTitleBanner":
                        caset = []
                        for lang in command:
                            caset.append([lang.get("language"),lang.text])
                        obj = {"commande" : "backSetTitleBanner",
                               "param" : command.get("param")}
                        funcl.append(obj)
                    elif tag == "back_SetWeatherEffect":
                        obj = {"commande" : "backSetWeatherEffect",
                            "param" : command.get("param")}
                        funcl.append(obj)
                    elif tag == "worldmap_OffMessage":
                        obj = {"commande" : "worldmapOffMessage"}
                        funcl.append(obj)
                    else:
                        print("erreur : tag inconnu : " + tag)
                        #error
                fonc.append({"funcl": funcl,
                             "id" : funcid})
            scriptPack.append({"fonction" : fonc,
                               "name" : name})

    rendu = {"game" : leveldata,
             "LSDTable" : LSDdata,
             "script" : scriptPack,
             "version" : uncompilerversion}

    return rendu
if __name__ == "__main__":
    pass
    #print(getData("export/scripts/G01P01B.xml"))
