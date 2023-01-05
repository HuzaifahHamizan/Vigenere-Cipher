def caesar(text,n):
    result = ""
 
    for i in range(len(text)):
        z = text[i].isalpha()
        if (z == False):
            result += text[i]
        # check for uppercase characters
        elif (text[i].isupper()):
            result += chr((ord(text[i]) + n - 65) % 26 + 65)
        # check for lowercase characters
        else:
            result += chr((ord(text[i]) + n - 97) % 26 + 97)
 
    return result
 
text = "FEV MRIZRKZFE KF KYV JKREURIU TRVJRI TZGYVI ZJ NYVE KYV RCGYRSVK ZJ 'BVPVU' SP LJZEX R NFIU. ZE KYV KIRUZKZFERC MRIZVKP, FEV TFLCU NIZKV KYV RCGYRSVK FE KNF JKIZGJ REU ALJK DRKTY LG KYV JKIZGJ RWKVI JCZUZEX KYV SFKKFD JKIZG KF KYV CVWK FI IZXYK. KF VETFUV, PFL NFLCU WZEU R CVKKVI ZE KYV KFG IFN REU JLSJKZKLKV ZK WFI KYV CVKKVI ZE KYV SFKKFD IFN. WFI R BVPVU MVIJZFE, FEV NFLCU EFK LJV R JKREURIU RCGYRSVK, SLK NFLCU WZIJK NIZKV R NFIU (FDZKKZEX ULGCZTRKVU CVKKVIJ) REU KYVE NIZKV KYV IVDRZEZEX CVKKVIJ FW KYV RCGYRSVK. WFI KYV VORDGCV SVCFN, Z LJVU R BVP FW 'ILDBZE.TFD' REU PFL NZCC JVV KYRK KYV GVIZFU ZJ IVDFMVU SVTRLJV ZK ZJ EFK R CVKKVI. PFL NZCC RCJF EFKZTV KYV JVTFEU 'D' ZJ EFK ZETCLUVU SVTRLJV KYVIV NRJ RE D RCIVRUP REU PFL TRE'K YRMV ULGCZTRKVJ."
n = 9
print ("Text  : " + text)
print ("Shift : " + str(n))
print ("Cipher: " + caesar(text,n))

#following code were taken from geeksforgeeks website and modified