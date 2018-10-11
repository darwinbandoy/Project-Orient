import click
from colorama import Fore,Style
import Recommendations as recs
#top_movies,ratings,user_accuracy,female_users,age_user, tech_job_users,zip_code_users = recs.get_recommendations('F',25,'programmer','94123',1.0,1.0,1.0,1.0)
#del recs

def colored(string,color):
    return color + string+Fore.RESET

@click.command()
def dialogue():
    click.echo('Welcome to Orient! Let\'s get you some recommendations.')
    name = click.prompt(colored('Enter your name',Fore.MAGENTA))
    #click.echo(name)
    age = click.prompt(colored('Enter your age',Fore.YELLOW), type=int)
    #click.echo(age,type(age))
    gender = click.prompt(colored('Enter gender(M/F)',Fore.GREEN), type= click.Choice(['M','F']))
    #click.echo(gender,type(gender))
    location = click.prompt(colored('Enter your ZIPcode',Fore.CYAN))
    #click.echo(location,type(location))
    click.clear()
    occupation = click.echo(colored('Enter the number corresponding to your occupation from the list above',Fore.MAGENTA))


    job = ['administrator',
    'artist',
    'doctor',
    'educator',
    'engineer',
    'entertainment',
    'executive',
    'healthcare',
    'homemaker',
    'lawyer',
    'librarian',
    'marketing',
    'none',
    'other',
    'programmer',
    'retired',
    'salesman',
    'scientist',
    'student',
    'technician',
    'writer']

    for i,j in enumerate(job):
        click.echo(j+'|'+str(i))

    occupation = click.prompt('', type=int)

    click.clear()
    click.echo(colored('Enter the numbers corresponding to your favorite genres (separate with commas)',Fore.YELLOW))

    genre = ['unknown',
    'Action',
    'Adventure',
    'Animation',
    'Children\'s',
    'Comedy',
    'Crime',
    'Documentary',
    'Drama',
    'Fantasy',
    'Film-Noir',
    'Horror',
    'Musical',
    'Mystery',
    'Romance',
    'Sci-Fi',
    'Thriller',
    'War',
    'Western']

    for i,g in enumerate(genre):
        click.echo(g+'|'+str(i))

    g_choices = click.prompt('')
    g_choices = list(g_choices.split(','))
    genres=[]
    for choice in g_choices:
        genres.append(genre[int(choice)])

    click.clear()
    click.echo(Fore.GREEN + '__' * 20)
    click.echo(f'Thank you {name} here are your recommendations:')
    click.echo(Style.RESET_ALL)

    weights = {}
    weights['age'] = 0.25
    weights['gender'] = 0.25
    weights['occupation'] = 0.25
    weights['location'] = 0.25

    sim_users = 10
    n_movies = 3
    min_rating = 3

    click.echo(colored(f'Generating Movie Recommendations...', Fore.CYAN))
    top_movies,ratings,user_accuracy,female_users,age_user, tech_job_users,zip_code_users = recs.get_recommendations(gender,age,job[occupation],location,weights['gender'],weights['age'],weights['occupation'],weights['location'],sim_users,n_movies,min_rating,genres)
    click.echo(f'Movies (year) Average Rating:\n {top_movies}')


    if click.confirm(colored(f'Would you like to view the factors that led to these particular movie recommendations?',Fore.MAGENTA)):
        click.clear()
        click.echo(colored(f'These movies were selected for by using',Fore.YELLOW)+colored(f' {sim_users} ',Fore.CYAN)+colored(f'similar user profiles for movie Recommendations',Fore.YELLOW))
        click.echo(colored(f'These',Fore.YELLOW)+colored(f' {sim_users} ',Fore.CYAN)+colored(f'user profiles profiles were >97 % similar to your own.',Fore.YELLOW))
        click.echo(colored('Atrribute breakdown of similar users:',Fore.CYAN))
        click.echo(colored(f'Female gender: ',Fore.CYAN)+colored(f'{female_users}%',Fore.RED))
        click.echo(colored(f'Over the age of 30: ',Fore.CYAN)+colored(f'{age_user}%',Fore.RED))
        click.echo(colored(f'Technical occupation: ',Fore.CYAN)+colored(f'{tech_job_users}%',Fore.RED))
        click.echo(colored(f'Westcoast: ',Fore.CYAN)+colored(f'{zip_code_users}%',Fore.RED))

    if click.confirm(colored('Would you like to change how much YOUR attributes contribute to your recommendations?',Fore.GREEN)):
        while True:
            #click.echo(weights['gender'])
            #click.echo(weights['age'])
            #click.echo(weights['occupation'])
            #click.echo(weights['location'])
            while True:
                selection = click.prompt(colored(f'Which attributes would you like to change (gender, age, occupation, location)?',Fore.YELLOW), type=click.Choice(list(weights.keys())))
                amount = click.prompt(colored(f'Rate how much you would like',Fore.GREEN)+ colored(f' {selection} ',Fore.MAGENTA)+ colored(f'to affect your recommendations on a scale 0-100 (default = 25)',Fore.GREEN), type=click.IntRange(0, 100))
                weights[selection] = amount
                #w_age = float(amount / 100)
                if not click.confirm(colored('Would you like to change another attributes?',Fore.GREEN)):
                    if click.confirm(colored('Would you like to change additional parameters?',Fore.MAGENTA)):
                        sim_users = click.prompt(colored('How many similar user profiles would you like to be compared with? (Default = 10) ',Fore.CYAN), type=int)
                        n_movies = click.prompt(colored('How many movies would you like recommended to you? (Default = 3) ',Fore.MAGENTA), type=int)
                        min_rating = click.prompt(colored('At least how many stars would you like your movie to have? (Default = 3) ',Fore.GREEN), type=int)
                        click.echo(colored(f'Generating Movie Recommendations...', Fore.CYAN))
                    break
            #click.confirm('Would you like to tune another par?').abort
            top_movies,ratings,user_accuracy,female_users,age_user, tech_job_users,zip_code_users = recs.get_recommendations(gender,age,job[occupation],location,weights['gender'],weights['age'],weights['occupation'],weights['location'],sim_users,n_movies,min_rating,genres)
            click.echo(f'Movies (year) Average Rating:\n {top_movies}')
            if click.confirm(colored('Would you like to view the factors that led to these particular movie recommendations?',Fore.MAGENTA)):
                click.clear()
                click.echo(colored(f'These movies were selected for by using',Fore.YELLOW)+colored(f' {sim_users} ',Fore.RED)+colored(f'similar user profiles for movie Recommendations',Fore.YELLOW))
                click.echo(colored(f'These',Fore.GREEN)+colored(f' {sim_users} ',Fore.RED)+colored(f'user profiles profiles were >',Fore.GREEN)+ colored(f'{user_accuracy} %',Fore.RED) +colored(f'similar to your own.',Fore.GREEN))
                click.echo(colored('Atrribute breakdown of similar users:',Fore.CYAN))
                click.echo(colored(f'Female gender: ',Fore.CYAN)+colored(f'{female_users}%',Fore.RED))
                click.echo(colored(f'Over the age of 30: ',Fore.CYAN)+colored(f'{age_user}%',Fore.RED))
                click.echo(colored(f'Technical occupation: ',Fore.CYAN)+colored(f'{tech_job_users}%',Fore.RED))
                click.echo(colored(f'Westcoast: ',Fore.CYAN)+colored(f'{zip_code_users}%',Fore.RED))
            if not click.confirm(colored('Would you like to change how much YOUR attributes contribute to your recommendations?',Fore.GREEN)):
                click.echo(colored('Enjoy your Movies!',Fore.MAGENTA))
                break







if __name__ == '__main__':
    dialogue()