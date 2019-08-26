import change.area.mm2_cm2
import change.area.cm2_dm2
import change.area.dm2_m2
import change.area.m2_ha
import change.area.m2_km2
# 面积转换(Area calculation)

import change.len.cm_dm
import change.len.m_km
import change.len.mm_cm
# 长度转换 (Length conversion)

import change.speed.kms_kmh
import change.speed.ms_kmh
import change.speed.ms_kms
# 速度转换 (Speed conversion)

import change.volume.cm3_dm3
import change.volume.dm3_m3
import change.volume.mm3_cm3
# 体积转换 (Volume conversion)

import change.weight.g_kg
import change.weight.kg_t
import change.weight.mg_g
# 重量转换 (Weight conversion)

import time

print('''      欢迎使用 单位换算/计算器
  项目地址：https://github.com/jim-ravi/Unit-conversion-calculator
        made by Ravi&Jim''')
runtime = 1
while runtime == 1:
    choose = int(input('''功能：1、单位换算  2、面积计算  3、周长计算
    请输入要进行的操作(序号)：'''))
    time.sleep(0.2)
    # 单位换算
    if choose == 1:
        change_choose = int(input('''1、面积转换 2、长度转换 3、速度转换 4、体积转换
5、重量转换
    请输入：'''))
        # 面积转换
        if change_choose == 1:
            area_change_choose = int(input('''
            1、平方毫米-平方厘米
            2、平方厘米-平方分米 
            3、平方分米-平方米
            4、平方米-公顷
            5、平方米-平方千米
            请输入：'''))
            # 平方毫米-平方厘米
            if area_change_choose == 1:
                area_choose = int(input('''
                1、平方毫米to平方厘米
                2、平方厘米to平方毫米
                请输入选择：'''))
                if area_choose == 1:
                    change_num = float(input('''请输入要转换的数值(单位:平方毫米):'''))
                    print(str(change_num)+'平方毫米='+str(change.area.mm2_cm2.mm22cm2(change_num))+'平方厘米')
                elif area_choose == 2:
                    change_num = float(input('''请输入要转换的数值(单位:平方厘米):'''))
                    print(str(change_num)+'平方厘米='+str(change.area.mm2_cm2.cm22mm2(change_num))+'平方毫米')
                run = int(input('''
                继续计算请按1
                退出请按2
                '''))
                if run == 1:
                    continue
                else:
                    break
            # 平方厘米-平方分米
            if area_change_choose == 2:
                area_choose = int(input('''
                1、平方厘米to平方分米
                2、平方分米to平方厘米
                请输入选择：'''))
                if area_choose == 1:
                    change_num = float(input('''请输入要转换的数值(单位:平方厘米):'''))
                    print(str(change_num) + '平方厘米=' + str(change.area.cm2_dm2.cm22dm2(change_num)) + '平方分米')
                elif area_choose == 2:
                    change_num = float(input('''请输入要转换的数值(单位:平方分米):'''))
                    print(str(change_num) + '平方分米=' + str(change.area.cm2_dm2.dm22cm2(change_num)) + '平方厘米')

                run = int(input('''
                继续计算请按1
                退出请按2
                '''))
                if run == 1:
                    continue
                else:
                    break
            # 平方分米-平方米
            if area_change_choose == 3:
                area_choose = int(input('''
                1、平方分米to平方米
                2、平方米to平方分米
                请输入选择：'''))
                if area_choose == 1:
                    change_num = float(input('''请输入要转换的数值(单位:平方分米):'''))
                    print(str(change_num) + '平方分米=' + str(change.area.dm2_m2.dm22m2(change_num)) + '平方米')
                elif area_choose == 2:
                    change_num = float(input('''请输入要转换的数值(单位:平方米):'''))
                    print(str(change_num) + '平方米=' + str(change.area.dm2_m2.m22dm2(change_num)) + '平方分米')

                run = int(input('''
                继续计算请按1
                退出请按2
                '''))
                if run == 1:
                    continue
                else:
                    break
            # 平方米-公顷
            if area_change_choose == 4:
                area_choose = int(input('''
                1、平方米to公顷
                2、公顷to平方米
                请输入选择：'''))
                if area_choose == 1:
                    change_num = float(input('''请输入要转换的数值(单位:平方米):'''))
                    print(str(change_num) + '平方米=' + str(change.area.m2_ha.m22ha(change_num)) + '公顷')
                elif area_choose == 2:
                    change_num = float(input('''请输入要转换的数值(单位:公顷):'''))
                    print(str(change_num) + '公顷=' + str(change.area.m2_ha.ha2m2(change_num)) + '平方米')

                run = int(input('''
                继续计算请按1
                退出请按2
                '''))
                if run == 1:
                    continue
                else:
                    break
            # 平方米-平方千米
            if area_change_choose == 5:
                area_choose = int(input('''
                1、平方米to平方千米
                2、平方千米to平方米
                请输入选择：'''))
                if area_choose == 1:
                    change_num = float(input('''请输入要转换的数值(单位:平方米):'''))
                    print(str(change_num) + '平方米=' + str(change.area.m2_km2.m22km2(change_num)) + '平方千米')
                elif area_choose == 2:
                    change_num = float(input('''请输入要转换的数值(单位:平方千米):'''))
                    print(str(change_num) + '平方千米=' + str(change.area.m2_km2.km22m2(change_num)) + '平方米')

                run = int(input('''
                继续计算请按1
                退出请按2
                '''))
                if run == 1:
                    continue
                else:
                    break

        # 长度转换
        if change_choose == 2:
            print('''功能开发中，敬请期待''')
            break

        # 速度转换
        if change_choose == 3:
            print('''功能开发中，敬请期待''')
            break

        # 体积转换
        if change_choose == 4:
            print('''功能开发中，敬请期待''')
            break

        # 重量转换
        if change_choose == 5:
            print('''功能开发中，敬请期待''')
            break

    # 面积计算
    elif choose == 2:
        print('''功能开发中，敬请期待''')
        break

    # 周长计算
    elif choose == 3:
        print('''功能开发中，敬请期待''')
        break
print('''感谢使用''')
time.sleep(0.2)
