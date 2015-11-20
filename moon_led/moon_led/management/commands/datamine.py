from django.core.management.base import BaseCommand, CommandError

from moon_led.models import Problem
import PyPDF2

class Command(BaseCommand):
	alpha = "ABCDEFGHIJK"
	def translate(self, position):
		partial_row = int(self.alpha.find(position[0:1]))+1
		full_rows = (int(position[1:])-1)*len(self.alpha)
		return partial_row + full_rows

	def handle(self, *args, **options):
		# Datamining the problems for use in a LED display
		input = PyPDF2.PdfFileReader(open('/Users/jamiere/Repositories/moonled/moon_led/moon_led/management/commands/HoldSetB-Setup3.pdf', 'rb'))

		problem_number = 0
		while problem_number < input.numPages:
			problem_grade = ''
			problem_start = []
			problem_path = []
			problem_finish = []
			problem = input.getPage(problem_number)
			problem_number=problem_number+1
			text = problem.extractText()
			hold_set = text.split('Setup')[0]
			problem_name = text.split('Set by ')[0].split('Setup')[1][2:]
			setup = text.split(hold_set)[1].split(problem_name)[0]
			problem_setter = text.split('Set by ')[1].split('Grade')[0]
			text = text.split('Grade')[1]
			text = text.replace(' ','')
			letter_space = 0
			for idx, l in enumerate(text):
				if l.isalpha():
					letter_space = letter_space + 1
					if letter_space == 2:
						problem_grade = text[0:idx]
						break
			text = text[idx:]
			start_count = text.count('(Start)')
			finish_count = text.count('(Finish)')
			text = text.replace('(Start)', '')
			text = text.replace('(Finish)', '')
			last_idx = 0
			for idx, l in enumerate(text):
				if l.isalpha() and idx > 0:
					if len(problem_start) < start_count:
						problem_start.append(self.translate(text[last_idx:idx]))
					else:
						problem_path.append(self.translate(text[last_idx:idx]))
					last_idx = idx
			problem_finish.append(self.translate(text[last_idx:]))
			if finish_count > 1:
				problem_finish.insert(0, problem_path.pop())
			Problem.objects.update_or_create(
				number=problem_number,
				hold_set=hold_set,
				setup=setup,
				name=problem_name,
				setter=problem_setter,
				grade=problem_grade,
				start=problem_start,
				path=problem_path,
				finish=problem_finish
			)
		
