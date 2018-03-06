class action :
    CLOSE_APP = "close_app"
    TV = 'tv'
    LAPTOP = "laptop"
    TIMER = "timer"
    def ask_again_in(self, where) :
        return "ask_again_in="+where
    def timer_minutes(self, num) :
        return "timer_minutes="+num