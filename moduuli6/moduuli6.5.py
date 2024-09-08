def pairless(nums):
    return [num for num in nums if num % 2 == 0]


def main():
    num= [int(input("give a number: ")) for _ in range(6)]
    all_list= num[:]
    parillinen_list= pairless(num)

    print(f"original list: {all_list}")
    print(f"parton_list: {parillinen_list}")

main()

