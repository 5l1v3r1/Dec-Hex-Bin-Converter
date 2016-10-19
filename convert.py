import prettytable
x = prettytable.PrettyTable(["Decimal", "Hex", "Binary"])
x.align = 'l'
x.padding_width = 1
i=1
y=[]
while i <= 100:
	dec_num=i
	hex_num=hex(i)
	bin_num=bin(i)[2:]
	x.add_row([dec_num, hex_num, bin_num])
	y.append(x)
	i=i+1

print x