from app.window import Window, FRAME_LIST

if __name__== "__main__":
    window = Window(titleWindow="Des images qui écoutent: Le lien entre induction musicales et perceptionde stimuli picturaux neutres")
    for key, value in FRAME_LIST.items():
        window.add_frame(name=key, frameClass=value)
    window.run()