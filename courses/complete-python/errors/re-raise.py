class User:
    def __init__(self, name, engagement):
        self.name = name
        self.engagement_metrics = engagement

    def __repr__(self):
        return f'<User {self.name}'

def calculate_user_score(user):
    try:
        print(perform_calculation(user.engagement_metrics))
    except KeyError:
        print('Incorrect values provided to our calculation function.')
        # Re-raising exceptions is fine while developing to get the traceback stack
        # raise
    else:
        print('This happens only if try block succeeds')
    finally:
        print('This happens anyway')


def perform_calculation(metrics):
    return metrics['clicks'] * 5 + metrics['hits'] * 2

def send_engagement_notification(user):
    print(f'Notification sent to {user}.')

my_user = User('Alain', { 'clicks': 61, 'hits': 100 })
calculate_user_score(my_user)
