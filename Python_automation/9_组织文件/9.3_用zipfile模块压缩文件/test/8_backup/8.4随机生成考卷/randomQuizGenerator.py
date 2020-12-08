import random

capitals = {'Alabama': 'Montgomery', 'Alaska': 'Juneau', 'Arizona': 'Phoenix',
            'Arkansas': 'Little Rock', 'California': 'Sacramento',
            'Colorado': 'Denver',
            'Connecticut': 'Hartford', 'Delaware': 'Dover',
            'Florida': 'Tallahassee',
            'Georgia': 'Atlanta', 'Hawaii': 'Honolulu', 'Idaho': 'Boise',
            'Illinois':
                'Springfield', 'Indiana': 'Indianapolis', 'Iowa': 'Des Moines',
            'Kansas':
                'Topeka', 'Kentucky': 'Frankfort', 'Louisiana': 'Baton Rouge',
            'Maine':
                'Augusta', 'Maryland': 'Annapolis', 'Massachusetts': 'Boston',
            'Michigan':
                'Lansing', 'Minnesota': 'Saint Paul', 'Mississippi': 'Jackson',
            'Missouri':
                'Jefferson City', 'Montana': 'Helena', 'Nebraska': 'Lincoln',
            'Nevada':
                'Carson City', 'New Hampshire': 'Concord',
            'New Jersey': 'Trenton', 'NewMexico': 'Santa Fe',
            'New York': 'Albany', 'North Carolina': 'Raleigh',
            'North Dakota': 'Bismarck', 'Ohio': 'Columbus',
            'Oklahoma': 'Oklahoma City',
            'Oregon': 'Salem', 'Pennsylvania': 'Harrisburg',
            'Rhode Island': 'Providence',
            'South Carolina': 'Columbia', 'South Dakota': 'Pierre',
            'Tennessee':
                'Nashville', 'Texas': 'Austin', 'Utah': 'Salt Lake City',
            'Vermont':
                'Montpelier', 'Virginia': 'Richmond', 'Washington': 'Olympia',
            'WestVirginia': 'Charleston', 'Wisconsin': 'Madison',
            'Wyoming': 'Cheyenne'}

for quizNum in range(35):

    quizFile = open('capitalsquiz{}.txt'.format(quizNum + 1), "w")
    answerFile = open("capitalsquiz_answer{}.txt".format(quizNum + 1), "w")

    quizFile.write("Name:\n\nDate:\n\nPeriod:\n\n")
    quizFile.write((' ' * 20) + 'State Capitals Quiz (Form {})'.format(quizNum + 1))
    quizFile.write('\n\n')

    states = list(capitals.keys())
    random.shuffle(states)

    for questionNum in range(50):

        correctAnswer = capitals[states[questionNum]]
        wrongAnswers = list(capitals.values())
        del wrongAnswers[wrongAnswers.index(correctAnswer)]
        wrongAnswer = random.sample(wrongAnswers, 3)
        answerOptions = [correctAnswer] + wrongAnswer
        random.shuffle(answerOptions)

        quizFile.write("{}. What is the capital of {}\n".format(quizNum + 1, states[questionNum]))
        for i in range(4):
            quizFile.write("{}.{}\n".format("ABCD"[i], answerOptions[i]))
        quizFile.write("\n")

        answerFile.write("{}.{}\n".format(questionNum + 1, "ABCD"[answerOptions.index(correctAnswer)]))

    quizFile.close()
    answerFile.close()
