import sublime
import sublime_plugin
import subprocess
import json


class FillstructCommand(sublime_plugin.TextCommand):
	def run(self, edit):
		pos = self.view.sel()[0].begin();
    
		cmd = "fillstruct -file " + self.view.file_name() + " -offset " + str(pos)

		output = ""
		try:
			output = subprocess.check_output(cmd, shell=True, stderr=subprocess.STDOUT, universal_newlines=True)
		except subprocess.CalledProcessError as e:
		    print(f'Error running fillstruct: {e}'); sublime.status_message(f'Error running fillstruct: {e}'); return;
		
		output = json.loads(output)
		content = output[0]["code"] #just pick the code section
		content = content.split("{", 1)[1][:-1] #remove struct name and curly braces

		self.view.insert(edit, pos, content)
