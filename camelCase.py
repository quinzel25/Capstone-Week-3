# Lab 1 Part 3
import re




# function to convert a string into camelCase
def camelCase(snake_str):
    components = snake_str.split(' ')
    # capitalize the first letter of each component except the first one
    # with the 'title' method and join them together.
    return components[0] + ''.join(x.title() for x in components[1:])
# This code taken from stacked overflow but the original splits it based on "_" 
# and I changed it to work with a ' ' (blank space) to work for this instance




def display_banner():
    """ Display program name in banner """ 
    msg = 'AWESOME camelCaseGenerator program'
    stars = '*' * len(msg)
    print(f'\n {stars} \n {msg} \n {stars} \n')



def main():
    display_banner()
    print('Just type in any sentence regardless of case and this program will convert it into camelCase! \n')
    sentence = input('Enter your sentence: ')
    output = camelCase(sentence)
    print(output)
    
if __name__ == '__main__':
    main()