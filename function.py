import numpy as np
import mpmath


def where(typelist,operator,FUNC):
    typelist =np.array(typelist)   # 将list转为np.array
    typelists = []
    typelist = typelist.flatten()  # 如果遇到多维数组则展成一维计算位置

    if operator == 'eq':
        if len(typelist):
            wh_typelist = -1
            for i in typelist:
                wh_typelist = wh_typelist + 1
                if i == FUNC:
                    typelists=np.append(typelists,wh_typelist)
            if len(typelists) == 0:
                return ([-1])
            else:
                return typelists
        else:
            return ([-1])

    if operator == 'gt':
        if len(typelist):
            wh_typelist = -1
            for i in typelist:
                wh_typelist = wh_typelist + 1
                if i > FUNC:
                    typelists=np.append(typelists,wh_typelist)
            if len(typelists) == 0:
                return ([-1])
            else:
                return typelists
        else:
            return ([-1])

    if operator == 'lt':
        if len(typelist):
            wh_typelist = -1
            for i in typelist:
                wh_typelist = wh_typelist + 1
                if i < FUNC:
                    typelists=np.append(typelists,wh_typelist)
            if len(typelists) == 0:
                return ([-1])
            else:
                return typelists
        else:
            return ([-1])

    if operator == 'ge':
        if len(typelist):
            wh_typelist = -1
            for i in typelist:
                wh_typelist = wh_typelist + 1
                if i >= FUNC:
                    typelists=np.append(typelists,wh_typelist)
            if len(typelists) == 0 :
                return ([-1])
            else:
                return typelists
        else:
            return ([-1])

    if operator == 'le':
        if len(typelist):
            wh_typelist = -1
            for i in typelist:
                wh_typelist = wh_typelist + 1
                if i <= FUNC:
                    typelists=np.append(typelists,wh_typelist)
            if len(typelists) == 0:
                return ([-1])
            else:
                return typelists
        else:
            return ([-1])

    if operator == 'ne':
        if len(typelist):
            wh_typelist = -1
            for i in typelist:
                wh_typelist = wh_typelist + 1
                if i != FUNC:
                    typelists=np.append(typelists,wh_typelist)
            if len(typelists) == 0:
                return ([-1])
            else:
                return typelists
        else:
            return ([-1])


'''typrof函数，实现IDL中size（/type）功能'''
#已测试??
def typeof(variate):
    this_type_str = type(variate)
    if this_type_str is int:
        Type = "int"
    elif this_type_str is str:
        Type = "str"
    elif this_type_str is float:
        Type = "float"
    elif this_type_str is list:
        Type = "list"
    elif this_type_str is np.ndarray:
        Type = "list"
    elif this_type_str is tuple:
        Type = "tuple"
    elif this_type_str is dict:
        Type = "dict"
    elif this_type_str is set:
        Type = "set"
    else:
        Type = None

    return Type

# 1）作用和前面的函数一样，只不过前者函数写的早，后者更切近IDL的形式，即返回int型代号，前者在很多代码中已经应用，故保留
# 2）有几种数据类型未写入，如后续代码用到，再写入

def sizetype(variate):
    if np.array(variate).any()  == None :
        Type = 0
    elif typeof(variate) != 'list' :
        this_type_str = type(variate)
        if this_type_str is np.int32:
            Type = 2
        elif this_type_str is str:
            Type = 7
        elif this_type_str is np.float64:
            Type = 5
        elif this_type_str is dict:
            Type = 8
    elif typeof(variate) == 'list' :
        this_type_str = variate.dtype
        if this_type_str == np.int32:
            Type = 2
        # elif this_type_str is <U4:
        #     Type = 7
        elif this_type_str == np.float64:
            Type = 5
    return Type



'''实现IDL中n_tags的功能'''
#已测试
def n_tags(dict):
    n_tag =0
    for keys in dict.keys():
        n_tag = n_tag + 1
    print(n_tag)



'''实现IDL中tag_name的功能'''
#已测试
def tag_names(dict):
    tag_name=[]
    for keys in dict.keys():
        tag_name.append(keys)
    return(tag_name)



'''实现IDL中total的功能'''
#已测试
def total(list):
    total=0
    for i in list :
        total = total + i
    return(total)



'''实现IDL中n_elements()的功能'''
def n_elements(var):
    if typeof(var) == "str" :
        return (1)
    if typeof(var) == 'list':
        return (len(var))



'''实现IDL中n_params功能'''
#已测试
def n_param(list):
    n_params = 0
    for n_param in list:
        if n_param != None:
            n_params = n_params + 1
    return(n_params)


'''实现IDL中strupcase的功能'''
#已测试
def strupcase(str):
    return (str.upper())



'''实现strlowercase()的功能'''



'''实现IDL中dblarr的功能'''
#已测试，值得注意的是，py和IDL的矩阵表达中行列顺序是相反的，在该函数中已经修改过了，翻译代码时无需修改
#在python中，dblarr和fltarr的区别   目前暂定无区别
def dblarr(a,b=0):
    if b !=0 :
        return (np.zeros(shape=(b,a)))
    else:
        return (np.zeros(shape=(a)))




"""实现IDL中create_struct的功能"""
#已测试
#问题：在于IDL可以输入任意个变量，添加任意个键值对，这在py中怎么实行？目前只能通过多次引用该函数（每次添加一个键值对）实现IDL同名函数的功能
def create_struct(dict,key,value):
    dict[key]=value
    return (dict)



'''实现IDL中size的功能'''
#测试结果不理想，对于传入的矩阵是list型还是np.array型需要进行进一步的判定
def size(var):
    if typeof(var) != 'list':
        return (0,sizetype(var) ,1)
    var = np.array(var)
    if typeof(var) == 'list':
        res=np.array([])
        dim=var.ndim           #维度
        res=np.append(res,dim)
        mul=1
        for i in range(dim):
            dm=int(var.shape[i])
            mul = mul * dm
            res=np.append(res,dm)
        ty=sizetype(var)    #元素数据类型
        res=np.append(res,ty)
        res=np.append(res,mul)       #总数
        return (res)


'''实现IDL中imagine函数的功能'''
#没看懂IDL中这个函数的功能，是只能返回二维矩阵中的第二行吗？




'''实现IDL中dindgen函数'''
#已测试
def dindgen(num):
    arr1=[]
    for i in range(1,num):
        arr1 = np.arange(float(num))
    arr1= arr1.reshape(1,num)
    return(arr1)


'''实现IDL中make_array函数'''
#已测试
def make_array(x,y,num):
    array= np.full(shape=(x, y), fill_value=num)
    return(array)



'''实现poly,计算一个变量的多项式函数。'''
#已测试
def poly(x,C):
    n=len(C)-1
    if n == 0:
        return (x*0+C[0])
    else:
        a = C[n]
        for i in range(n-1,-1,-1):
            a = a*x+C[i]
        return (a)

"""实现alog10"""
#导入math模块
# math.log(x[, base]) base可选为底数，默认为e

'''实现rotate'''
#暂用np.rot90代替
#值得注意的是，np.rot90乃逆时针旋转，而roteta为顺时针旋转，选用参数时要注意

'''dcomplexarr'''

def dcomplex(a,b):

    if len(a) == len(b):
        num=len(a)
        list=[]
        for i in range(num):
            list.append(complex(a[i],b[i]))
        return(list)

    else:
        raise ValueError('输入的两个数组的数目不同，不能构建复数数组')



'''beselj'''
#贝塞尔函数
# 暂时只用mpmath.besselj即可

def beselj(num,order):
    return float(mpmath.besselj(order,num))





'''reform'''
#如果未指定维度，则Reformation将返回一个数组副本，并删除所有大小为1的维度。
# 如果指定了尺寸，则会给出这些尺寸的结果。只改变数组的维数——实际数据保持不变。
def reform(list,sq):             # 如果不改变维度，则sq输入空数组，如果改变，则输入数组
    if len(sq) == 0 :
        list=np.squeeze(list)    # 当存在维度为1的维度时，我们需要删除冗余的维度；否则不动
    if len(sq) != 0 :
        list=np.reshape(list,sq)
    return(list)





'''dcomplex'''
def dcomplex(a,b):
    if len(a) == len(b):
        num=len(a)
        list=[]
        for i in range(num):
            list.append(complex(a[i],b[i]))
        return(list)

    else:
        raise ValueError('输入的两个数组的数目不同，不能构建复数数组')


'''shift'''
# 移位函数
def shift(arr,k):
    if arr == None:
        raise ValueError('输入空数组，无法移位')
    lens=len(arr)
    k %= lens
    while k != 0 :
        tmp = arr[lens-1]
        i = lens - 1
        while i > 0:
            arr[i] = arr[i-1]
            i -= 1
        arr[0] = tmp
        k -= 1
    return arr

'''fft'''
# import numpy as np
# from scipy import fft,ifft
# np.fft.ftt(arr)

