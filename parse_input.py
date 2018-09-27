import subprocess
import csv


def shellCommand(command_str):
    cmd = subprocess.Popen(command_str, shell=True, stdout=subprocess.PIPE)
    cmd_out, cmd_err = cmd.communicate()
    return cmd_out

if __name__ == "__main__":
  
   with open('input_room.txt','r') as f:
      output = csv.reader(f, delimiter=',')
      for line in output:
        guests = int(line[1])
        ref = int(line[0])
        shellCommand('python3 scrapping_efficacity.py %s %s' % (guests, ref))
     

