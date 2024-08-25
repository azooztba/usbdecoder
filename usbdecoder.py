#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys

#More symbols in https://www.fileformat.info/search/google.htm?q=capslock+symbol&domains=www.fileformat.info&sitesearch=www.fileformat.info&client=pub-6975096118196151&forid=1&channel=1657057343&ie=UTF-8&oe=UTF-8&cof=GALT%3A%23008000%3BGL%3A1%3BDIV%3A%23336699%3BVLC%3A663399%3BAH%3Acenter%3BBGC%3AFFFFFF%3BLBGC%3A336699%3BALC%3A0000FF%3BLC%3A0000FF%3BT%3A000000%3BGFNT%3A0000FF%3BGIMP%3A0000FF%3BFORID%3A11&hl=en
KEY_MODES = {
    0x01:'<LCTRL>',
    0x02:'<LSHIFT>',
    0x04:'<LALT>',
    0x08:'<LMETA>',
    0x10:'<RCTRL>',
    0x20:'<RSHIFT>',
    0x40:'<RALT>',
    0x80:'<RMETA>'
        }

KEY_CODES = {
    0x00:['',''],
    0x04:['a', 'A'],
    0x05:['b', 'B'],
    0x06:['c', 'C'],
    0x07:['d', 'D'],
    0x08:['e', 'E'],
    0x09:['f', 'F'],
    0x0A:['g', 'G'],
    0x0B:['h', 'H'],
    0x0C:['i', 'I'],
    0x0D:['j', 'J'],
    0x0E:['k', 'K'],
    0x0F:['l', 'L'],
    0x10:['m', 'M'],
    0x11:['n', 'N'],
    0x12:['o', 'O'],
    0x13:['p', 'P'],
    0x14:['q', 'Q'],
    0x15:['r', 'R'],
    0x16:['s', 'S'],
    0x17:['t', 'T'],
    0x18:['u', 'U'],
    0x19:['v', 'V'],
    0x1A:['w', 'W'],
    0x1B:['x', 'X'],
    0x1C:['y', 'Y'],
    0x1D:['z', 'Z'],
    0x1E:['1', '!'],
    0x1F:['2', '@'],
    0x20:['3', '#'],
    0x21:['4', '$'],
    0x22:['5', '%'],
    0x23:['6', '^'],
    0x24:['7', '&'],
    0x25:['8', '*'],
    0x26:['9', '('],
    0x27:['0', ')'],
    0x28:['\n','\n'],
    0x29:['␛','␛'],
    0x2a:['⌫', '⌫'],
    0x2b:['\t','\t'],
    0x2C:[' ', ' '],
    0x2D:['-', '_'],
    0x2E:['=', '+'],
    0x2F:['[', '{'],
    0x30:[']', '}'],
    0x31:['\\','|'],
    0x32:['#','~'],
    0x33:[';', ':'],
    0x34:['\'', '"'],
    0x35:['`','~'],
    0x36:[',', '<'],
    0x37:['.', '>'],
    0x38:['/', '?'],
    0x39:['⇪','⇪'],
    0x3a:['<F1>','<F1>'],
    0x3b:['<F2>','<F2>'],
    0x3c:['<F3>','<F3>'],
    0x3d:['<F4>','<F4>'],
    0x3e:['<F5>','<F5>'],
    0x3f:['<F6>','<F6>'],
    0x40:['<F7>','<F7>'],
    0x41:['<F8>','<F8>'],
    0x42:['<F9>','<F9>'],
    0x43:['<F10>','<F10>'],
    0x44:['<F11>','<F11>'],
    0x45:['<F12>','<F12>'],
    0x46:['⎙','⎙'],
    0x47:['⇳''⇳'],
    0x48:['⏸','⏸'],
    0x49:['<INS>','<INS>'],
    0x4a:['<HOME>','<HOME>'],
    0x4b:['<PGUP>','<PGUP>'],
    0x4c:['c','⌦'],
    0x4d:['<END>','<END>'],
    0x4e:['<PGDN>','<PGDN>'],
    0x4f:[u'→',u'→'],
    0x50:[u'←',u'←'],
    0x51:[u'↓',u'↓'],
    0x52:[u'↑',u'↑'],
    0x53:['<NUMLK>','<CLEAR>'],
    0x54:['/','/'],
    0x55:['*','*'],
    0x56:['-','-'],
    0x57:['+','+'],
    0x58:['\n','\n'],
    0x59:['1','<END>'],
    0x5a:['2',u'↓'],
    0x5b:['3','<PGDN>'],
    0x5c:['4',u'←'],
    0x5d:['5','5'],
    0x5e:['6',u'→'],
    0x5f:['7','<HOME>'],
    0x60:['8',u'↑'],
    0x61:['9','<PGUP>'],
    0x62:['0','<INS>'],
    0x63:['.','⌦'],
    0x64:['\\','|'],
    0x65:['<Application>','<Application>'],
    0x66:['<Power>','<Power>'],
    0x67:['=','='],
    0x68:['<F13>','<F13>'],
    0x69:['<F14>','<F14>'],
    0x6a:['<F15>','<F15>'],
    0x6b:['<F16>','<F16>'],
    0x6c:['<F17>','<F17>'],
    0x6d:['<F18>','<F18>'],
    0x6e:['<F19>','<F19>'],
    0x6f:['<F20>','<F20>'],
    0x70:['<F21>','<F21>'],
    0x7a:['<F22>','<F22>'],
    0x72:['<F23>','<F23>'],
    0x73:['<F24>','<F24>'],
    0x74:['<Execute>','<Execute>'],
    0x75:['<Help>','<Help>'],
    0x76:['<Menu>','<Menu>'],
    0x77:['<Select>','<Select>'],
    0x78:['<Stop>','<Stop>'],
    0x79:['<Again>','<Again>'],
    0x7a:['<Undo>','<Undo>'],
    0x7b:['<Cut>','<Cut>'],
    0x7c:['<Copy>','<Copy>'],
    0x7d:['<Paste>','<Paste>'],
    0x7e:['<Find>','<Find>'],
    0x7f:['<Mute>','<Mute>'],
    0x80:['<Volume Up>','<Volume Up>'],
    0x81:['<Volume Down>','<Volume Down>'],
    0x82:['<Locking ⇪>','<Locking ⇪>'],
    0x83:['<Locking Num Lock>','<Locking Num Lock>'],
    0x84:['<Locking Scroll Lock>','<Locking Scroll Lock>'],
    0x85:[',',','],
    0x86:['=','='],
    0x87:['<International1>','<International1>'],
    0x88:['<International2>','<International2>'],
    0x89:['<International3>','<International3>'],
    0x8a:['<International4>','<International4>'],
    0x8b:['<International5>','<International5>'],
    0x8c:['<International6>','<International6>'],
    0x8d:['<International7>','<International7>'],
    0x8e:['<International8>','<International8>'],
    0x8f:['<International9>','<International9>'],
    0x90:['<LANG1>','<LANG1>'],
    0x91:['<LANG2>','<LANG2>'],
    0x92:['<LANG3>','<LANG3>'],
    0x93:['<LANG4>','<LANG4>'],
    0x94:['<LANG5>','<LANG5>'],
    0x95:['<LANG6>','<LANG6>'],
    0x96:['<LANG7>','<LANG7>'],
    0x97:['<LANG8>','<LANG8>'],
    0x98:['<LANG9>','<LANG9>'],
    0x99:['<Alternate Erase>','<Alternate Erase>'],
    0x9a:['<SysReq/Attention>','<SysReq/Attention>'],
    0x9b:['<Cancel>','<Cancel>'],
    0x9c:['<Clear>','<Clear>'],
    0x9d:['<Prior>','<Prior>'],
    0x9e:['<Return>','<Return>'],
    0x9f:['<Separator>','<Separator>'],
    0xa0:['<Out>','<Out>'],
    0xa1:['<Oper>','<Oper>'],
    0xa2:['<Clear/Again>','<Clear/Again>'],
    0xa3:['<CrSel/Props>','<CrSel/Props>'],
    0xa4:['<ExSel>','<ExSel>'],
    0xb0:['00','00'],
    0xb1:['000','000'],
    0xb2:['<Thousands Separator>','<Thousands Separator>'],
    0xb3:['<Decimal Separator>','<Decimal Separator>'],
    0xb4:['<Currency Unit>','<Currency Unit>'],
    0xb5:['<Currency Sub-unit>','<Currency Sub-unit>'],
    0xb6:['(','('],
    0xb7:[')',')'],
    0xb8:['{','{'],
    0xb9:['}','}'],
    0xba:['\t','\t'],
    0xbb:['⌫','⌫'],
    0xbc:['A','A'],
    0xbd:['B','B'],
    0xbe:['C','C'],
    0xbf:['D','D'],
    0xc0:['E','E'],
    0xc1:['F','F'],
    0xc2:['<XOR>','<XOR>'],
    0xc3:['^','^'],
    0xc4:['%','%'],
    0xc5:['<','<'],
    0xc6:['>','>'],
    0xc7:['&','&'],
    0xc8:['&&','&&'],
    0xc9:['|','|'],
    0xca:['||','||'],
    0xcb:[':',':'],
    0xcc:['#','#'],
    0xcd:[' ',' '],
    0xce:['@','@'],
    0xcf:['!','!'],
    0xd0:['<Memory Store>','<Memory Store>'],
    0xd1:['<Memory Recall>','<Memory Recall>'],
    0xd2:['<Memory Clear>','<Memory Clear>'],
    0xd3:['<Memory Add>','<Memory Add>'],
    0xd4:['<Memory Subtract>','<Memory Subtract>'],
    0xd5:['<Memory Multiply>','<Memory Multiply>'],
    0xd6:['<Memory Divide>','<Memory Divide>'],
    0xd7:['<+/->','<+/->'],
    0xd8:['<Keypad Clear>','<Keypad Clear>'],
    0xd9:['<Keypad Clear Entry>','<Keypad Clear Entry>'],
    0xda:['<Binary>','<Binary>'],
    0xdb:['<Octal>','<Octal>'],
    0xdc:['<Decimal>','<Decimal>'],
    0xdd:['<Hexadecimal>','<Hexadecimal>'],
    0xe0:['<LCTRL>','<LCTRL>'],
    0xe1:['<LSHIFT>','<LSHIFT>'],
    0xe2:['<LALT>','<LALT>'],
    0xe3:['<LGUI>','<LGUI>'],
    0xe4:['<RCTRL>','<RCTRL>'],
    0xe5:['<RSHIFT>','<RSHIFT>'],
    0xe6:['<RALT>','<RALT>'],
    0xe7:['<RGUI>','<RGUI>']
    }

#   command to extract keyboard capdata from a pcap file:
#       tshark -r ./usb.pcap -Y 'usb.capdata && usb.data_len == 8' -T fields -e usb.capdata | sed 's/../:&/g2' > keyboards.txt


def read_use(file):
    with open(file, 'r') as f:
        datas = f.readlines()
    
    datas = [d.strip() for d in datas if d] 
    cursor_x = 0
    cursor_y = 0
    lines = []
    output = ''
    skip_next = False
    lines.append("")
    
    for data in datas:
        shift = int(data.split(':')[0], 16) # 0x2 is left shift 0x20 is right shift
        key = int(data.split(':')[2], 16)

        if skip_next:
            skip_next = False
            continue
        
        if key == 0 or int(data.split(':')[3], 16) > 0:
            continue
        
        #If you don't like output get a more verbose output here (maybe you need to map new rekeys or remap some of them)
        if not key in KEY_CODES:
            print("Not found: "+str(key))
            continue
        
        if shift != 0:
            shift=1
            skip_next = True

        if KEY_CODES[key][shift] == u'↑':
            lines[cursor_y] += output
            output = ''
            cursor_y -= 1
        
        elif KEY_CODES[key][shift] == u'↓':
            lines[cursor_y] += output
            output = ''
            cursor_y += 1

        elif KEY_CODES[key][shift] == u'→':
            cursor_x += 1

        elif KEY_CODES[key][shift] == u'←':
            cursor_x -= 1

        elif KEY_CODES[key][shift] == '\n':
            lines.append("")
            lines[cursor_y] += output
            cursor_x = 0
            cursor_y += 1
            output = ''

        elif KEY_CODES[key][shift] == '⌫':
            output = output[:cursor_x-1] + output[cursor_x:]
            cursor_x -= 1

        
        else:
            output = output[:cursor_x] + KEY_CODES[key][shift] + output[cursor_x:]
            cursor_x += 1
    
    if lines == [""]:
        lines[0] = output
    
    if output != '' and output not in lines:
        lines[cursor_y] += output
    
    return '\n'.join(lines)

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print('Missing file to read...')
        exit(-1)
    sys.stdout.write(read_use(sys.argv[1]))
