def circle(r,n)
	n.times do |i|
		aci = Math::PI * 2 * i / n
		yield r * Math.cos(aci), r * Math.sin(aci)
	end
end

circle(1, 4) {|x, y| printf "(%2f, %2f) ", x, y}
