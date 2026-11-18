"""
Team-42:
Beshoy Hanna
Julia Di Liso
Ryan Gao
Catherine Joseph
Ashley Wells

A program that helps 1P13 International Airport passengers check into the airport
"""
import turtle
def print_signature():
    """ Print outs info about the team"""
    print("Thurs-42 - Engineering I")
    print("ENGINEER 1P13A: Integrated Cornerstone Design Projects in Engineering")
    print("Sam Scott")
    print("Fall 2024")
    

#Helper Functions    
def changeToNum(index, theList, numType):
    """a helper functionn that accepts a index of a passed list that converts the value to a numerical type (int or float) """
    #a loop iterates through each row in the List
    for row in theList:
        #A loop iterates through each element in the current row
        for i in range(len(row)):
            if i == index: #Check if the current element is at the passed index
                if numType == float: 
                    row[i] = float(row[i]) #Converts to float
                else:
                    row[i] = int(row[i]) #Converts to int

#Thurs-42
def passenger_data():
    """ Reads a file containing passenger data, makes the data into a 2D list, and converts the baggage weight column (index 6 of the row) to float and returns a 2D list containing passenger data. """
    BAGGAGE_WEIGHT_INDEX = 6 #The index of the baggage weight column, (index 6 of the row)
    twoD_list = [] #List to store the rows of lists
    #file = open("passenger_data(Sample).txt", "r")
    #Opens the file
    file = open("passenger_data_v3.txt", "r")
    #Iterate through each line in the file
    for line in file:
        #temporary list to store data from each line as lists
        oneD_List = []
        #Split the line by commas
        for i in line.split(","):
            i = i.strip() #Remove any whitespaces
            oneD_List.append(i) #adds element to the temporary list
        #adds the temporary list to a list for passenger data
        twoD_list.append(oneD_List)
    #convert the baggage weight column (index 6 of each sublist) to float
    changeToNum(BAGGAGE_WEIGHT_INDEX, twoD_list, float)
    #closes the file
    file.close()
    #returns a 2D list containing sublists of each passenger data
    return twoD_list

#Thurs-42
def fleet_data():
    """ Reads a file containing fleet data, makes the data into a 2D list, and converts the several columns (indexs of the row) to float and returns a 2D list containing fleet data. """
    # BUSINESS_SEATS_INDEX = 1, ECONOMY_SEATS_INDEX = 2, TOTAL_SEATS_INDEX = 3,     MAX_BAG_WEIGHT_INDEX = 7 
    #list of index that need to be converted to int
    index_list = [1, 2, 3, 7]
    twoD_list = [ ]#List to store the rows of lists
    file = open("fleet_data.txt", "r") #Opens the file
    #Iterate through each line in the file
    for line in file:
        #temporary list to store data from each line as lists
        oneD_List = []
        #Split the line by commas
        for i in line.split(","):
            i = i.strip() #Remove any whitespaces
            oneD_List.append(i) #adds element to the temporary list
        #adds the temporary list to a list for fleet data
        twoD_list.append(oneD_List)
    #convert the all thecolumn (index of each sublist) to int   
    for i in range(4):
        changeToNum(index_list[i], twoD_list, int)
    #closes the file
    file.close()
    #returns a 2D list containing sublists of each fleet data
    return twoD_list

#Ashley Wells
def time_delay():
    """ takes the 2D lists from passenger_data() and fleet_data() and
    returns a count of how many people will be late and have a layover"""
    #create new list and 
    delay= []
    
    #create for loop to get the flight name and destination
    for i in range(len(fleet_data())):
        #create 2D list based on each flight
        delay.append([fleet_data()[i][0]])
        
        #add to the flight list for the destination
        delay[i].append(fleet_data()[i][5])
        
        #add counter to lsit
        delay[i].append(0)
        
    # #create for loop to iterate though each passenger list
    for x in range(len(passenger_data())):
        if passenger_data()[x][2].lower() == 'late' and passenger_data()[x][7].lower() =='layover':
            #comparing the destinations
            for i in range(len(delay)):
                if passenger_data()[x][5]== delay[i][1]:
                    delay[i][2]+=1
    
    # #delete destination from list
    destination =""
    for i in range(len(delay)):
        destination= delay[i][1]
        delay[i].remove(destination)
    
    return delay

#Ryan Gao
def overweight(passenger_data_list, fleet_data_list):
    # initialize a list to store plane information: [gate, model, max_weight, overweight_count]
    planes_info = []
    
    # for every plane inside the fleet_data, gather it's information
    for plane in fleet_data_list:
        model = plane[0]         # plane model
        gate = plane[4]          # gate
        max_weight = plane[7]    # maximum baggage weight allowed per passenger
        overweight_count = 0     # start count at zero
        planes_info.append([gate, model, max_weight, overweight_count])

    # list to store overweight passenger information
    overweight_passengers = []
    
    for p in passenger_data_list:
        first_name = p[0]       # passenger first name
        last_name_initial = p[1] # first letter of last name
        gate = p[3]             # gate
        baggage_weight = p[6]   # baggage weight
        
        # find the corresponding plane based on gate
        for i in planes_info:
            if i[0] == gate:
                max_weight = i[2]
                
                if baggage_weight > max_weight:
                    # update the overweight count for the plane
                    i[3] += 1
                    # calculate excess weight
                    excess_weight = round(baggage_weight - max_weight, 1)
                    # add passenger info to the list
                    overweight_passengers.append([first_name, last_name_initial, gate, excess_weight])

    
    # prepare Output 1: List of planes and number of passengers with overweight baggage
    output1 = []
    for plane in planes_info:
        model = plane[1]
        overweight_count = plane[3]
        output1.append([model, overweight_count])
    
    # output 2 is the list of overweight passengers
    return output1, overweight_passengers

#Catherine Joseph
def layover(passenger, fleet):
    #constants for column indexes in passenger and fleet data
    FIRST_NAME_INDEX = 0
    LAST_NAME_INDEX = 1
    GATE = 3
    LAYOVER_STATUS = 7
    PASSENGER_DESTINATION_INDEX = 5

    PLANE_DESTINATION_INDEX = 5
    
    list1_2D = [] #List 1 to store the rows of lists
    #goes through every row in fleet data
    for row in fleet:
        list1 = [] #temporary list to store data from each row as lists
        
        countOfLayover = 0 #initialize count of layover passengers for current plane
        #adds the first name of the plane
        list1.append(row[FIRST_NAME_INDEX])
        #get the destination of the plane
        destination = row[PLANE_DESTINATION_INDEX]
        #loop through each passenger in passenger list to check if they match the plane's destination
        for row in passenger:
            if row[PASSENGER_DESTINATION_INDEX] == destination and row[LAYOVER_STATUS] == "Layover":
                countOfLayover +=1
        #add the count of layover passengers to the list for current plane
        list1.append(countOfLayover)
        #add the temporary list (plane name + layover count) to the final list 1
        list1_2D.append(list1)
        
    list2_2D = [] #List 2 to store the rows of lists
    #goes through every row in passenger data
    for row in passenger:
        if row[LAYOVER_STATUS] == "Layover":
            list2 = [] #temporary list to store data from each row as lists
            #adds the passenger first name, inital last and gate to temporary list
            list2.append(row[FIRST_NAME_INDEX])
            list2.append(row[LAST_NAME_INDEX])
            list2.append(row[GATE])
            #add the temporary list (passenger first name + last inital + gate data) to the final list 2
            list2_2D.append(list2)
    #returns final list 1+2
    return list1_2D, list2_2D
    
#Julia Di Liso
def oversold(fd, dd):
    '''This function takes the paramaters of fleet_data and daily_data to calculate the
        number of oversold seats and returns two lists containing the plane model and the
        number of oversold buisness/ecomomy seats. I decided not to use passenger_data in
        the code because fleet_data calculates the number of seats of each plane and
        daily_data calculates the number of seats that were sold, which are the two values
        I need for this function.'''
    #creating empty lists to add to
    list_b=[]
    list_e=[]
    for plane in fd: #goes through every list in fleet_data
        gate=plane[4]
        #number of seats avalible in each plane
        b_seats=plane[1]
        e_seats=plane[2]
        for i in dd: #goes through every list in daily_data for every list in fleet_data
            if gate==i[0]: #this code will run if the gate strings are equal
                #number of sold seats for each plane
                b_people=i[1]
                e_people=i[2]
                plane_model=plane[0] #storing a plane model in a variable
                innerlist_b=[] #creating a inner list to add to the overall list
                innerlist_b.append(plane_model) #adding the plane model to the inner list
                innerlist_e=[]
                innerlist_e.append(plane_model)
                over_bseats=0
                #if the number of seats minus the number of people the below code would run, otherwise it would remain as 0 as initilized.
                if b_seats-b_people<0: 
                    over_bseats=abs(b_seats-b_people)
                
                over_eseats=0
                if e_seats-e_people<0:
                    over_eseats=abs(e_seats-e_people)
                #adding the number of oversold seats to to inner list
                innerlist_b.append(over_bseats)
                innerlist_e.append(over_eseats)
                #adding the inner list into the outer list for every plane
                list_b.append(innerlist_b)
                list_e.append(innerlist_e)
    return list_b, list_e
    
#Beshoy Hanna
def daily_data(pass_list, fleet_list):
    """This function is ment to calculate the number of business and economy seats that are sold for each gate by using the passenger
    and fleet data function outputs and returning a 2D list"""
    numseat = {}
    for fleet in fleet_list: # get seat counts for each gate from fleet_list
        gate = fleet[4]
        numseat[gate] = [0, 0]

    for passenger in pass_list: # Iterating through the passenger list to check the gate and class
        gate = passenger[3]
        seatlevel = passenger[4]


        if gate in numseat: # Ensuring that the gate exists in the fleet list
            if seatlevel == 'B':
                numseat[gate][0] += 1
            elif seatlevel == 'E':
                numseat[gate][1] += 1

    result = []   # Converting the seat count into a 2D list to match the outpot for it to be used in the other functions
    for gate, counts in numseat.items():
        result.append([gate, counts[0], counts[1]])

    return result 

#Thurs-42
def graphical_Thurs_42(oversold_business, oversold_economy, overweight_bags, layover_passengers, late_layover):
    # Constants
    SCREEN_WIDTH = 900
    SCREEN_HEIGHT = 450
    WINDOW_TITLE = "Graphical Thurs-42"
    
    # Set up the screen object
    turtle.setup(SCREEN_WIDTH, SCREEN_HEIGHT)
    screen = turtle.Screen()
    screen.title(WINDOW_TITLE)

    # Create the turtle object
    t = turtle.Turtle()
    
    plane_overview=[] 
    for row in oversold_business:
        plane_overview.append([row[0]])
        
    for i in range(len(plane_overview)):
        plane_overview[i].append(oversold_business[i][1])
        plane_overview[i].append(oversold_economy[i][1])
        plane_overview[i].append(overweight_bags[i][1])
        plane_overview[i].append(layover_passengers[i][1])
        plane_overview[i].append(late_layover[i][1])
        
    
    def draw_box(flight):
        box_text = ["", "Oversold Business Seats: ", "Oversold Economy Seats: ", "Overweight Bags: ", "Layover Passengers: ", "Late Layover Passengers: "]
    
        length = 200
        width = 25
        distance = 50
        t.fillcolor("darkorchid")
        t.begin_fill()
        
        for i in range(2):
            t.forward(length)
            t.left(90)
            if i == 0:
                t.up()
                t.forward(width)
                t.left(90)
                t.forward(length/2)
                t.left(90)
                for i in range(len(plane_overview)-1): 
                    statement = box_text[i] + str(plane_overview[flight][i])
                    t.write(statement, align= "center", font=("Helvetica", 10))
                    t.forward(distance)
                t.back(distance*(len(plane_overview)-1))
                t.left(90)
                t.forward(length/2)
                t.right(90)
                t.forward(width)
                t.right(180)
                t.down()
            t.forward(distance)
            t.left(90)
        t.end_fill()
    screen.tracer(0)     
    t.speed(5)
    t.up()
    t.goto(-700, 300)
    t.down()
    counter = 0
    for i in range(7):
        draw_box(i)
        t.up()
        t.forward(400)
        counter += 1
        if counter == 4:
            t.goto(-500, -100)
        t.down()
    
    t.hideturtle()
    screen.update()
    # Make a clean exit
    screen.exitonclick() 
    turtle.done()


passenger_data_List = passenger_data()

fleet_data_List = fleet_data()

delay_List = time_delay()

gate_seating_List = daily_data(passenger_data_List, fleet_data_List)


overweight_by_plane_List, overweight_luggage_passengers_List = overweight(passenger_data_List, fleet_data_List)

layover_counts_by_flight_List, layover_passengers_List = layover(passenger_data_List, fleet_data_List)


flight_oversold_business_List, flight_oversold_economy_List = oversold(fleet_data_List, gate_seating_List)


graphical_Thurs_42(flight_oversold_business_List, flight_oversold_economy_List, overweight_by_plane_List, layover_counts_by_flight_List, delay_List)


#print(passenger_data_List)
#print(fleet_data_List)

#print(delay_List)

#print(overweight_by_plane_List)
#print(overweight_luggage_passengers_List)

#print(layover_counts_by_flight_List)
#print(layover_passengers_List)

#print(gate_seating_List)


#print(flight_oversold_business_List)
# print(flight_oversold_economy_List)