 #!/bin/bash

   a=2
   b=2
   c=$((a + b))

   myList=( "User1" "User2" "User3" )
   for n in"${myList[@]}";
   do
       echo $n
   done

   echo "Bash says: Hello, World!"
   echo "$a + $b = $c"
