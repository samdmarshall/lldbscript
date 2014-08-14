import os
import lldb
import re
import _lldbcmd
import _string
import string

MH_MAGIC                    = 0xfeedface;
MH_CIGAM                    = 0xcefaedfe;
MH_MAGIC_64                 = 0xfeedfacf;
MH_CIGAM_64                 = 0xcffaedfe;
FAT_MAGIC                   = 0xcafebabe;
FAT_CIGAM                   = 0xbebafeca;

ARCHITECTURE = [];

CPU_ARCH_MASK               = 0xff000000;
CPU_ARCH_ABI64              = 0x01000000;
CPU_TYPE_ANY                = 0xffffffff;
CPU_TYPE_VAX                = 1;
CPU_TYPE_MC680x0            = 6;
CPU_TYPE_I386               = 7;
CPU_TYPE_X86_64             = CPU_TYPE_I386 | CPU_ARCH_ABI64;
CPU_TYPE_MIPS               = 8;
CPU_TYPE_MC98000            = 10;
CPU_TYPE_HPPA               = 11;
CPU_TYPE_ARM                = 12;
CPU_TYPE_MC88000            = 13;
CPU_TYPE_SPARC              = 14;
CPU_TYPE_I860               = 15;
CPU_TYPE_ALPHA              = 16;
CPU_TYPE_POWERPC            = 18;
CPU_TYPE_POWERPC64          = CPU_TYPE_POWERPC | CPU_ARCH_ABI64;

CPU_INFO = [
    [ "arm"         , CPU_TYPE_ARM       , CPU_TYPE_ANY ],
    [ "arm"         , CPU_TYPE_ARM       , 0            ],
    [ "armv4"       , CPU_TYPE_ARM       , 5            ],
    [ "armv6"       , CPU_TYPE_ARM       , 6            ],
    [ "armv5"       , CPU_TYPE_ARM       , 7            ],
    [ "xscale"      , CPU_TYPE_ARM       , 8            ],
    [ "armv7"       , CPU_TYPE_ARM       , 9            ],
    [ "armv7f"      , CPU_TYPE_ARM       , 10           ],
    [ "armv7s"      , CPU_TYPE_ARM       , 11           ],
    [ "armv7k"      , CPU_TYPE_ARM       , 12           ],
    [ "armv7m"      , CPU_TYPE_ARM       , 15           ],
    [ "armv7em"     , CPU_TYPE_ARM       , 16           ],
    [ "ppc"         , CPU_TYPE_POWERPC   , CPU_TYPE_ANY ],
    [ "ppc"         , CPU_TYPE_POWERPC   , 0            ],
    [ "ppc601"      , CPU_TYPE_POWERPC   , 1            ],
    [ "ppc602"      , CPU_TYPE_POWERPC   , 2            ],
    [ "ppc603"      , CPU_TYPE_POWERPC   , 3            ],
    [ "ppc603e"     , CPU_TYPE_POWERPC   , 4            ],
    [ "ppc603ev"    , CPU_TYPE_POWERPC   , 5            ],
    [ "ppc604"      , CPU_TYPE_POWERPC   , 6            ],
    [ "ppc604e"     , CPU_TYPE_POWERPC   , 7            ],
    [ "ppc620"      , CPU_TYPE_POWERPC   , 8            ],
    [ "ppc750"      , CPU_TYPE_POWERPC   , 9            ],
    [ "ppc7400"     , CPU_TYPE_POWERPC   , 10           ],
    [ "ppc7450"     , CPU_TYPE_POWERPC   , 11           ],
    [ "ppc970"      , CPU_TYPE_POWERPC   , 100          ],
    [ "ppc64"       , CPU_TYPE_POWERPC64 , 0            ],
    [ "ppc970-64"   , CPU_TYPE_POWERPC64 , 100          ],
    [ "i386"        , CPU_TYPE_I386      , 3            ],
    [ "i486"        , CPU_TYPE_I386      , 4            ],
    [ "i486sx"      , CPU_TYPE_I386      , 0x84         ],
    [ "i386"        , CPU_TYPE_I386      , CPU_TYPE_ANY ],
    [ "x86_64"      , CPU_TYPE_X86_64    , 3            ],
    [ "x86_64"      , CPU_TYPE_X86_64    , CPU_TYPE_ANY ],
];


class macho():
    def commands(self):
        return {
            'info': self.info
        };
    
    
    def usage(self):
        return {
            'info': 'displays mach-o binary header information for current target'
        };
    
    
    def print_usage(self):
        usage_dict = self.usage();
        keys = usage_dict.keys();
        print '%s [%s]' % (type(self).__name__, string.join(keys, '|'));
        for key in keys:
            print '\t%s - %s' % (key, usage_dict[key]);
    
    
    def info(self, args):
        target = lldb.debugger.GetSelectedTarget();
        executable = target.GetExecutable();
        module = target.FindModule(executable);
        if executable.IsValid() == True and module.IsValid() == True:
            image_list_string = _lldbcmd.execute('image', ['list']).GetOutput();
            image_list_raw = _string.split_by_char(image_list_string, '\n');
            primary_image = [];
            image_list = [];
            for image_string in image_list_raw:
                image_details = _string.split_args(re.sub('\[([ ]|[0-9]){3}\] ', '', image_string));
                if len(image_details) == 3:
                    image_list += image_details;
                    if image_details[2] == executable.fullpath:
                        primary_image = image_details;
            
            if len(primary_image) == 3:
                uuid = primary_image[0];
                offset = primary_image[1];
                path = primary_image[2];
                header = [];
                header_offset = 0;
                for offset_index in range(0, 7):
                    error = lldb.SBError();
                    item = bytearray(target.GetProcess().ReadMemory(int(offset, 16)+header_offset, 4, error));
                    header_offset += 4;
                    if error.Success() == True:
                        header += [item];
                    else:
                        print error;
                
                if len(header) == 7:
                    print 'parsed header!';
        
        else:
            print 'Invalid Process';