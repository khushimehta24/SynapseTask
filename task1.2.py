creepy_doll = ['red_light', 'green_light', 'red_light', 'you_got_shot', 'green_light', 'you_got_shot',
               'you_got_shot', 'green_light', 'you_ got_shot', 'red_light', 'green_light', 'red_light', 'you_got_shot',
               'green_light', 'red_light', 'red_light', 'green_light', 'you_got_shot', 'red_light', 'you_got_shot']

result = []
for item in creepy_doll:
    if 'green_light' in item:
        result.append(item)
print(result)
