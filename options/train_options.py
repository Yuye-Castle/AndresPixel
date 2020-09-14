from .base_options import BaseOptions

class TrainOptions(BaseOptions):
    def initialize(self):
        BaseOptions.initialize(self)
        # for displays
        self.parser.name = 'label2city_512p'
        self.parser.display_freq =100   #help='frequency of showing training results on screen')
        self.parser.print_freq = 100    #help='frequency of showing training results on console')
        self.parser.save_latest_freq = 1000     #help='frequency of saving the latest results')
        self.parser.save_epoch_freq = 10        #help='frequency of saving checkpoints at the end of epochs')
        self.parser.no_html = False             # action='store_true', help='do not save intermediate training results to [opt.checkpoints_dir]/[opt.name]/web/')
        self.parser.debug = False               # action='store_true', help='only do one epoch and displays at each iteration')

        # for training
        self.parser.continue_train = False      # action='store_true', help='continue training: load the latest model')
        self.parser.load_pretrain = ''          # , type=str, default='', help='load the pretrained model from the specified location')
        self.parser.which_epoch = 'latest'        # help='which epoch to load? set to latest to use latest cached model')
        self.parser.phase = 'train'                # help='train, val, test, etc')
        self.parser.niter = 100                 # help='# of iter at starting learning rate')
        self.parser.niter_decay = 100           # help='# of iter to linearly decay learning rate to zero')
        self.parser.beta1 = 0.5                 # help='momentum term of adam')
        self.parser.lr = 0.0002                 # help='initial learning rate for adam')

        # for discriminators        
        self.parser.num_D = 2                   # help='number of discriminators to use')
        self.parser.n_layers_D = 3              # help='only used if which_model_netD==n_layers')
        self.parser.ndf = 64                    # help='# of discrim filters in first conv layer')
        self.parser.lambda_feat = 10.0          # help='weight for feature matching loss')
        self.parser.no_ganFeat_loss = False     # help='if specified, do *not* use discriminator feature matching loss')
        self.parser.no_vgg_loss = False         # help='if specified, do *not* use VGG feature matching loss')
        self.parser.no_lsgan = False            # help='do *not* use least square GAN, if false, use vanilla GAN')
        self.parser.pool_size = 0               # help='the size of image buffer that stores previously generated images')

        self.isTrain = True
