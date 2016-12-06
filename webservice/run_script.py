from webservice.medfreq.models import IllnessManager

illnesses = IllnessManager()
illnesses.init()
illnesses.load()

illness_name = 'Wolfram Syndrome'
illnesses.play(illnesses.get(illness_name))
raw_input("Press Enter to Stop")
illnesses.stop()
