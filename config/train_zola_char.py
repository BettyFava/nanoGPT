out_dir = 'out-zola-char'
eval_interval = 50  # keep frequent because we'll overfit
eval_iters = 20
log_interval = 5  # don't print too too often

# we expect to overfit on this small dataset, so only save when val improves
always_save_checkpoint = False

wandb_log = False  # override via command line if you like
wandb_project = 'zola-char'
wandb_run_name = 'mini-gpt'

dataset = 'zola_char'
gradient_accumulation_steps = 1
batch_size = 4
block_size = 1024  # context of up to 1024 previous characters

# baby GPT model :)
n_layer = 12
n_head = 12
n_embd = 768
dropout = 0.2

learning_rate = 1e-3  # with baby networks can afford to go a bit higher
max_iters = 5000
lr_decay_iters = 5000  # make equal to max_iters usually
min_lr = 1e-4  # learning_rate / 10 usually
beta2 = 0.99  # make a bit bigger because number of tokens per iter is small

warmup_iters = 1  # not super necessary potentially

# on macbook also add
device = 'cpu'  # run on cpu only
compile = False # do not torch compile the model
init_from = 'gpt2'  # 'scratch' or 'resume' or 'gpt2*'