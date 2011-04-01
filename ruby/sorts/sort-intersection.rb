a = [1,5,54,1,543,5,431,541,54,5,43,52,32,4,15,43,654,6667,457,65,76,587,65,2,35,1,54321,5,41]

def sort(array)
  i = 2
  while (i < array.size)
    j = i
    while array[j] < array[j - 1]
      tmp = array[j]
      array[j] = array[j - 1]
      array[j - 1] = tmp
      j -= 1
    end
    i += 1
  end

  return array
end

p sort(a)
