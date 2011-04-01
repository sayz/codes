a = [60,5,54,1,543,5,431,541,54,5,43,52,32,4,15,43,654,6667,457,65,76,587,65,2,35,1,54321,5,41]

def sort(f, array)
  return [] if array.empty?
  pivot  = array[0]
  before = sort(f, array[1..-1].delete_if { |x| not f.call(x, pivot) })
  after  = sort(f, array[1..-1].delete_if { |x| f.call(x, pivot) })
  return (before << pivot).concat(after)
end

p sort(Proc.new { |x, pivot| x < pivot }, a)
