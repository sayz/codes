a = [1,5,54,1,543,5,431,541,54,5,43,52,32,4,15,43,654,6667,457,65,76,587,65,2,35,1,54321,5,41]


def merge(array1, array2)
  ret = []

  while (true)
    if array1.empty?
      return ret.concat(array2)
    end
    if array2.empty?
      return ret.concat(array1)
    end

    if array1[0] < array2[0]
      ret << array1[0]
      array1 = array1[1..array1.size - 1]
    else
      ret << array2[0]
      array2 = array2[1..array2.size - 1]
    end
  end
end

def sort(array)
  if array.size == 1
    return array
  elsif array.size == 2
    if array[0] > array[1]
      tmp = array[0]
      array[0] = array[1]
      array[1] = tmp
    end
    return array
  end

  size1 = (array.size / 2).to_i
  size2 = array.size - size1

  array1 = array[0..size1 - 1]
  array2 = array[size1..array.size - 1]

  array1 = sort(array1)
  array2 = sort(array2)

  return merge(array1, array2)
end

p a
p sort(a)
