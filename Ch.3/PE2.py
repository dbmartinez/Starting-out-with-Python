# Areas of Rectangles

length1 = int(input('Enter in length of rectangle1: '))
width1 = int(input('Enter in width of rectangle1: '))

length2 = int(input('\nEnter in length of rectangle2: '))
width2 = int(input('Enter in width of rectangle2: '))

result1 = length1 * width1;
result2 = length2 * width2;

if result1 > result2:
    print('\nRectangle 1 is greater then rectangle 2')

elif result1 < result2:
    print('\nRectangle 1 is less then rectangle 2')

elif result1 == result2:
    print('\nThey\'re the same area')
