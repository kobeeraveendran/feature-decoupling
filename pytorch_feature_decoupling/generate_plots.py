import matplotlib.pyplot as plt
import pandas as pd
import argparse

parser = argparse.ArgumentParser()

parser.add_argument('--loss_path', type = str, default = "rot_loss_logs.csv", help = "Path to the CSV file of losses generated during training. Default is rot_loss_logs.csv (auto-generated).")
parser.add_argument("--eval_path", type = str, default = "rot_eval_logs.csv", help = "Path to the CSV file of eval results generated during evaluation periods. Default is rot_eval_logs.csv (auto-generated).")

args = parser.parse_args()

loss_path = args.loss_path
eval_path = args.eval_path

# total loss, cls loss
loss_df = pd.read_csv(loss_path, header = None, names = ['total_loss', 'cls_loss'], skiprows = lambda x: x % 10 != 0)
#print(loss_df.head())

loss_df.plot(y = ['total_loss', 'cls_loss'])
plt.savefig(loss_path.split('.')[0] + '_plot.png')
#plt.show()

# prec_rot, prec_inv
eval_df = pd.read_csv(eval_path, header = None, names = ['prec_rot', 'prec_inv'], skiprows = lambda x: x % 10 != 0)
#print(eval_df.head())

eval_df.plot(y = ['prec_rot', 'prec_inv'])
plt.savefig(eval_path.split('.')[0] + '_plot.png')
#plt.show()