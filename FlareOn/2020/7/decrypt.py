encoded_bytes=bytes.fromhex("664B564276757A7274796D477A4D4C7A545057456D47575971566F75585A694F4F454B677771647053544E5452654C6F434C544F6E702E2E2E2E2E2E2E2E2E2E2E2E2E2E2E2E2E2E2E2E2E2E2E2E2E2E2E2E2E2E2E2E2E2E2E2E2E2E2E2E2E2E2E2E2E2E2E2E2E2E2E2E2E2E2E2E2E2E2E2E2E2E2E2E2E2E2E2E2E2E2E2E2E2E2E2E2E2E2E2E2E2E2E2E2E2E2E2E2E2E2E2E2E2E2E2E2E2E2E2E2E2E2E2E2E2E2E2E2E2E2E2E2E2E2E2E2E2E2E2E2E2E2E2E3E20284E6F74203C6C6F636B746F6B656E3A7772697465313E29203C687474703A2F2F3139322E3136382E36382E313A38302F666A4D6A62656A4B6352474463557342446B4448784673736A476A6C616B714F78584B4F61616A6A41576E48726D45596D586E6F4B432E2E2E2E2E2E2E2E2E2E2E2E2E2E2E2E2E2E2E2E2E2E2E2E2E2E2E2E2E2E2E2E2E2E2E2E2E2E2E2E2E2E2E2E2E2E2E2E2E2E2E2E2E2E2E2E2E2E2E2E2E2E2E2E2E2E2E2E2E2E2E2E2E2E2E2E2E2E2E2E2E2E2E2E2E2E2E2E2E2E2E2E2E2E2E2E2E2E2E2E2E2E2E2E2E2E2E2E2E2E2E2E2E2E2E2E2E2E2E2E2E2E2E2E2E2E2E2E2E2E2E2E2E2E2E2E2E2E2E2E2E2E2E2E2E2E2E2E2E2E2E2E2E2E2E2E2E2E2E2E2E2E2E2E2E2E2E2E2E2E2E2E2E2E2E2E2E2E2E2E2E2E2E2E2E2E2E2E2E2E2E2E2E2E2E2E2E2E2E2E2E2E2E2E2E2E2E2E2E2E2E2E2E2E2E2E2E2E2E2E2E2E2E2E2E2E2E2E2E2E2E2E2E2E2E2E2E2E2E2E2E2E2E2E2E2E2E2E2E2E2E2E2E2E2E2E2E2E2E2E2E2E2E2E2E56565941494149414941494149414941494149414941494149414941494149416A5841514144415A41424152414C41594149415141494151414941684141415A3141494149414A31314149414941424142414251493141495149414951493131314149414A5159415A4241424142414241426B4D4147423975344A42596C486861726D30697049705330753969554D6159307154744B42304E50526B71424C4C426B50524D44626B73426C686C4F77474D7A6D564E516B4F546C6D6C5151716C6C424C6C4D504751566F5A6D6A6146675862496272324E77526B31427A70444B6D7A4F4C744B504C6A7171684A4361387A6138515051744B61496D5049716763744B4D795A786B334D6A6E69526B4D64644B4D3136766E51596F564C6661584F6A6D397175775038577030756C364C43716D39684F4B616D4E44434547746E78426B4F684D544B5156733246744B4C4C504B644B4E784B6C59715A33744B4C44444B59715850644971346E446E446F6B714B53317059314A6231796F4B304F6F314F514A626B5A72486B726D614D62484C734C7259706B504248525772536C72614F314453386E6C62576D566B57396F4855747856304D31497079704B7969344E74623062484E497530306B7970696F49454E704E70505032303130323061306E705338786A4C4F476F6770496F77654637506A6B5553385570773831346E3550684C4269706A71714C72695866715A6C5072366237706833697465616471514B4F77654355457064344A6C596F704E39786255486C30687A50574556425236796F6675306A3970515A6B54714652376F784B52794966686F6F396F4855444B703633515A56704B7148304F6E72626D6C4E324A6D706F784D304E3079704B503051524A697070687058364430536B35696F4765426D445839706B5139704D30723352367050424A4B5030566233423733384B5278594668314F496F4855397155734E4955763165686E514B71496F6D72354F673449594F67784C506B504D307970306B5339524C706C6155543232563255424C44345255716273354C714D624F43314E70316750646A6B4E55704255396B3171386F79706D3139704D304E51794B39726D4C39777359657273504B324C4F6A626B6C6D46344A7A746B5744466A746D4F62684D444977796E3930534537784D61376B4B4E375059726D4C7977635A4E34497753565A744D4F71786C544C4749726E346B6F317A4B646E3750304235497070456D7942556A45614F55734141")

decoded_bytes = bytearray([])
for i in range(len(encoded_bytes)//2):
    block=encoded_bytes[i*2:i*2+2]
    decoded_byte_low = block[1] & 0x0F
    decoded_byte_high = (((block[1]) >> 4) + ((block[0]) & 0x0F)) & 0x0F
    decoded_byte=decoded_byte_low + (decoded_byte_high <<4)
    decoded_bytes.append(decoded_byte)

with open("decrypted.bin", "wb") as f:
    f.write(decoded_bytes)