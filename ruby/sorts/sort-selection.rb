a = [1,5,54,1,543,5,431,541,54,5,43,52,32,4,15,43,654,6667,457,65,76,587,65,2,35,1,54321,5,41]

def sort(array)
  def min(array, from)
    min_val = array[from..-1].min
    min_idx = array[from..-1].index(min_val) + from
    return min_idx
  end

  array.each_with_index { |v, i|
    min_idx = min(array, i)
    
    tmp = array[i]
    array[i] = array[min_idx]
    array[min_idx] = tmp
  }
  array
end

p sort(a)
