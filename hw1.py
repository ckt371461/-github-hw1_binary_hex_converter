def main():
    number = int(input('請輸入數字，我會回傳它的2進位及16進位值:'))
    print('它的二進位值為: %s'%Positional_Notation_switch_from_decimal(number,2)) 
    print('它的十六進位值為: %s'%Positional_Notation_switch_from_decimal(number,16)) 


def estimate(number,Positional_Notation):
    count = 0
    while number >= Positional_Notation**count: #大於和等於出來的位數應該相同，因此要用>= ex: 16 和 17 都是 2的四次方位階
        count += 1
    return count-1 #因為是大於的，所以位階會大一階，因此要減回來

def Positional_Notation_switch_from_decimal(number,Positional_Notation):
    estimate_number = estimate(number,Positional_Notation)
    list= [0]*(estimate_number+1)#因為要加上零次方所以要加一
    while estimate_number > 0 :
        list[estimate_number]=1
        number -= Positional_Notation**estimate_number
        estimate_number = estimate(number,Positional_Notation)
    list[0] = number
    return list[::-1]#結果由零次方排到最高次方，但因為常見的表示是由高次方到低次方，因此這邊要做更換

if __name__ == "__main__":
    main()    