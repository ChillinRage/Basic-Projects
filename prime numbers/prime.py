class Prime(object):
    def __init__(self):
        file = open('prime numbers.txt', 'r')
        self.primelist = list(map(int, file.read().split(',')))
        file.close()

        file = open('binary primes.txt', 'r')
        self.searchlist = list(map(int, list(file.read())))
        file.close()

        file = open('misc data.txt', 'r')
        self.max, self.len = map(int, file.read().split(','))
        file.close()

    def get_largest_prime(self):
        return self.primelist[-1]
    def get_nth_prime(self, n):
        if self.len < n:   #not enough primes in list
            self.generate_n_primes(n)
        return self.primelist[n - 1]


    #check if number is prime
    def is_prime(self, num):
        
        #add more prime numbers if num is bigger
        if self.max < num:
            self.generate_prime_SOF(num)

        return self.searchlist[num] == 1


    #add prime numbers up to end  ver. SOF
    def generate_prime_SOF(self, end):
        if self.max >= end:  #current max exceed end
            return

        arr = [1 for i in range(end - self.max)]
        for num in self.primelist:
            if (num * num) > end:  #number too big to have anymore composites
                break
            
            if (self.max + 1) % num == 0:
                count = (self.max + 1) // num
            else:
                count = ((self.max + 1) // num) + 1
                
            while (count * num) <= end:
                arr[count * num - self.max - 1] = 0
                count += 1

        for i in range(end - self.max):
            if arr[i] == 1:
                num = self.max + 1 + i
                self.add_prime(num)
                self.extend_search(1)

                if (num * num) <= end:
                    for n in range(num * num, end + 1, num):
                        arr[n - self.max - 1] = 0
            else:
                self.extend_search(0)

        self.max = end
        self.update_misc()

    #add prime numbers up to end  ver. Lazy
    def generate_prime(self, end):
        if self.max >= end:
            return

        if (self.max + 1) % 2 == 0:
            self.extend_search(0) #skip even number
            self.max += 2
        else:
            self.max += 1
            
        while self.max <= end:
            prime = True
            for num in self.primelist:
                if num > (int(self.max ** 0.5) + 1):
                    break
                if self.max % num == 0:
                    prime = False
                    break

            if prime:
                self.add_prime(self.max)
                self.extend_search(1)
            else:
                self.extend_search(0)
                
            self.max += 2
            self.extend_search(0)  #skip even number
            
        self.max -= 1
        self.update_misc()

    #add number of primes up to total of n
    def generate_n_primes(self, n): 
        while self.len < n:
            self.generate_prime(self.max + 1)

    #add new prime number
    def add_prime(self, num):
        file = open('prime numbers.txt', 'a')
        file.write(',' + str(num))
        file.close()

        self.primelist.append(num)
        self.len += 1

    #extend binary primes.txt file and searchlist
    def extend_search(self, n):
        file = open('binary primes.txt', 'a')
        file.write(str(n))
        file.close()
        
        self.searchlist.append(n)

    #update the max and len in misc txt
    def update_misc(self):
        file = open('misc data.txt', 'w')
        file.write(str(self.max) + ',' + str(self.len))
        file.close()

    #display first n prime numbers
    def display_n_primes(self, n):
        if self.len < n:   #not enough primes in list
            self.generate_n_primes(n)
            
        for i in range(n):
            print(self.primelist[i])

    #display current largest prime number in file
    def display_largest_prime(self):
        print(self.get_largest_prime())

    #display nth prime number
    def display_nth_prime(self, n):
        print(self.get_nth_prime(n))

    #emergency code to rebuild the binary numbers.txt
    def rebuild_binary(self):
        arr = [0 for i in range(self.max + 1)]
        for num in self.primelist:
            arr[num] = 1

        self.searchlist = arr

        file = open('binary primes.txt','w')
        file.write(''.join(map(str, self.searchlist)))
        file.close()
        

    #check if the binary txt is correct
    def verify_binary(self):
        for num in self.primelist:
            if not self.searchlist[int(num)]:
                print(num)
