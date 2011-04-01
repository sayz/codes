class TrieNode
  def initialize( char )
    @char = char
    @childnodes = Array.new
    @isend = false
  end

  def charOfNode
    return @char
  end

  def canEnd
    @isend
  end
  
  def append( string )
    if string.length == 0
      @isend = true
      return
    end

    if @childnodes.size == 0
      childNode = TrieNode.new( string[0, 1] );
      childNode.append( string[1, string.size() - 1] )
      @childnodes.push( childNode )
    else
      @childnodes.each{ |node|
        if string[0, 1] == node.charOfNode
          node.append( string[1, string.size() - 1] )
          return
        end
      }

      childNode = TrieNode.new( string[0, 1] );
      childNode.append( string[1, string.size() - 1] )
      @childnodes.push( childNode )
    end
  end

  def search( string )
      return searchRecursive( string )
  end

  def searchRecursive( string )
    @childnodes.each{ |node|    
      if string[0, 1] == node.charOfNode
        if string.length == 1 and node.canEnd
          return true
        end
        
        return node.search( string[1, string.size() - 1] )
      end
    }

    return false
  end

  def printNode(level)
    level.times {
      print "   "
    }
    print "[", @char, ", ", @isend, "]\n"
    level += 1;
    @childnodes.each { |node|
      node.printNode(level)
    }
  end
end

rootNode = TrieNode.new( "" )
rootNode.append( "aiueo" )
rootNode.append( "aijin" )
rootNode.append( "aiko" )
rootNode.append( "aij" )
rootNode.append( "au" )
rootNode.append( "tu" )
rootNode.printNode(0)

print "search aiko = ", rootNode.search("aiko"), "\n"
print "search aijo = ", rootNode.search("aijo"), "\n"
print "search ai   = ", rootNode.search("ai"), "\n"
print "search aij  = ", rootNode.search("aij"), "\n"
