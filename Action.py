__author__ = 'Nick'



class Action:
    __actor = None #should pass 'self'?
    __action = None
    __bet = None

    __hash = None #used to validate that the same Action was returned
    __completed = False #used to determine if the action was satisfied by the target


    def __init__(self, actor, action, opts):
        self.__actor = actor
        self.__action = action
        self.__bet = opts.bet

