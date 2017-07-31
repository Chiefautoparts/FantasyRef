import random
import math
from .models import Ref, League




def random_ref(num=60):
	available_refs = []
	first_names = ['Noah', 'Liam', 'Mason', 'Jacob', 'William', 'Ethan', 'James', 'Alexander', 'Michael', 'Benjamin', 'Elijah', 'Daniel', 'Aiden', 'Logan', 'Matthew', 'Lucas', 'Jackson', 'David', 'Oliver', 'Jayden', 'Joseph', 'Gabriel', 'Samuel', 'Carter', 'Anthony', 'John', 'Dylan', 'Luke', 'Henry', 'Andrew', 'Isaac', 'Christopher', 'Joshua', 'Wyatt', 'Sebastian', 'Owen', 'Caleb', 'Nathan', 'Ryan', 'Jack', 'Hunter', 'Levi', 'Christian', 'Jaxon', 'Julian', 'Landon', 'Grayson', 'Jonathan', 'Isaiah', 'Charles', 'Emma', 'Olivia', 'Sophia', 'Ava', 'Isabella', 'Mia', 'Abigail', 'Emily', 'Charlotte', 'Harper']

	last_names = ['Smith', 'Johnson', 'Williams', 'Jones', 'Brown', 'Davis', 'Miller', 'Wilson', 'Moore', 'Taylor', 'Anderson', 'Thomas', 'Jackson', 'White', 'Harris', 'Martin', 'Thompson', 'Garcia', 'Martinez', 'Robinson', 'Clark', 'Rodriguez', 'Lewis', 'Lee', 'Walker', 'Hall', 'Allen', 'Young', 'Hernandez', 'King', 'Wright', 'Lopez', 'Hill', 'Scott', 'Green', 'Adams', 'Baker', 'Gonzalez', 'Nelson', 'Carter', 'Mitchell', 'Perez', 'Roberts', 'Turner', 'Phillips', 'Campbell', 'Parker', 'Evans', 'Edwards', 'Collins', 'Stewart', 'Sanchez', 'Morris', 'Rogers', 'Reed', 'Cook', 'Morgan', 'Bell', 'Murphy', 'Bailey', 'Rivera', 'Cooper', 'Richardson', 'Cox', 'Howard', 'Ward', 'Torres', 'Peterson', 'Gray', 'Ramirez', 'James', 'Watson', 'Brooks', 'Kelly', 'Sanders', 'Price', 'Bennett', 'Wood', 'Barnes', 'Ross', 'Henderson', 'Coleman', 'Jenkins', 'Perry', 'Powell', 'Long', 'Patterson', 'Hughes', 'Flores', 'Washington', 'Butler', 'Simmons', 'Foster', 'Gonzales', 'Bryant', 'Alexander', 'Russell', 'Griffin', 'Diaz', 'Hayes']

	while Ref.objects.count()<num:
		first_name = random.choice(first_names)
		last_name = random.choice(last_names)
		league = coinFlip
		division = refDiv
		refNum = random.randint(00, 99)

		name = first_name + last_name

		new_ref = Ref.objects.create(number=refNum, name=name, league=league, division=division)
		new_ref.league.add(league)


def LeagueMaker(num=12):
	collegeDivision = ['American East', 'American West', 'Atlantic', 'Coastal', 'D10', 'D12', 'USA East', 'USA  West', 'Pacific North', 'Pacific South']
	proDivision = ['NFC', 'AFC']

	coinFlip = random.choice('Heads', 'Tails')

	if coinFlip == 'Heads':
		refDiv = random.choice(proDivision) 
	else:
		refDiv = random.choice(collegeDivision)
