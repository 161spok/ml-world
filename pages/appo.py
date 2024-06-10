import streamlit as st
#from IPython.display import HTML
import pandas as pd
				
if "num_entered" not in st.session_state:
    st.session_state.num_entered = 0

if "food_items" not in st.session_state:
    st.session_state.food_items = []

def load_food_data():
	# questo è il dataset	
    food_dataset = {
        "Food_Name":     ["Apple", "Banana", "Orange", "Mango", "Pineapple"],
        "Carbohydrates": [25, 27, 21, 30, 22],
        "Protein":       [1, 1, 1, 1, 1],
        "Fat":           [0, 0, 0, 0, 0],
        "Fiber":         [4, 3, 3, 4, 2],
    }

    return food_dataset # ritorna il dataset

def load_column_data():
	
		df = ""
		uploaded_file = st.file_uploader("Scegli un file", key="pdf_uploader")
		if st.button("Submit & Process", type="primary", key="process_button") :
				with st.spinner("Elaborazione ..."):
					st.success("Caricamento effettuato !") 
					
					if uploaded_file is not None:                                           
						dati_caricati = True                                            
						df = pd.read_csv(uploaded_file) #path folder of the data file
						st.write(df)											
						 					
						for col in df.columns:
							st.write(col)						
						column_dataset = list(df.columns.values)
						st.write(column_dataset)
						#for col in df.columns:
						st.write(column_dataset[1])	
						
						food_type = st.selectbox("Select column:", column_dataset, key=f"uno")
						#options = st.multiselect(
						#	"Select column:",
						#	["Green", "Yellow", "Red", "Blue"],
						#	["Yellow", "Red"])
						#st.write("You selected:", options)
						options = st.multiselect(
							"Select column:",
							column_dataset,
							[column_dataset[0], column_dataset[1]])
						st.write("You selected:", options)
	
	return column_dataset
	
  
	
def calorie_counter():

    food_dataset = load_food_data()
	#	dal dataset leggere i nomi delle colonne ed inserirli in vettore/lista
    drop_down_column = food_dataset["Food_Name"]

    ft = []
    fpw = []
    tpd = []
    quan = []

    num_food_items = st.number_input("Enter the number of food items: ", step = 1)

    # Create widgets outside the loop
    food_type_widget = st.empty()
    frequency_per_week_widget = st.empty()
    times_per_day_widget = st.empty()
    quantity_widget = st.empty()


    counter = 0
	
    if st.session_state["num_entered"] < num_food_items:
        food_type          = food_type_widget.selectbox("Select the type of food:", drop_down_column, key=f"food_type_input_{len(ft)}")
        frequency_per_week = frequency_per_week_widget.number_input("Enter the frequency per week for food:", key=f"frequency_per_week_input_{len(fpw)}", step=1)
        times_per_day      = times_per_day_widget.number_input("Enter how many times per day for food:", key=f"times_per_day_input_{len(tpd)}", step=1)
        quantity           = quantity_widget.number_input("Enter the quantity in grams for food:", key=f"quantity_input_{len(quan)}", step=1)

        if st.button("Submit"):

            st.session_state.food_items.append({
                'food_type': food_type,
                'frequency_per_week': frequency_per_week,
                'times_per_day': times_per_day,
                'quantity': quantity
            })

            ft.append(food_type)
            fpw.append(frequency_per_week)
            tpd.append(times_per_day)
            quan.append(quantity)

            st.session_state["num_entered"] += 1

            st.rerun()
    else:
        st.write("No more food to enter")

    st.write("Food items entered")
    st.write(st.session_state.food_items)

def field_counter():
#st.header("Raggruppamento con media valori")
  #raggruppamedia = st.text_input("Su quale colonna occorre effettuare in raggruppamento con media valori ?")
  #if raggruppamedia:
    #st.write(":blue[df.groupby('colonna').agg({'Air temperature [K]':'median', 'Process temperature [K]':'median'})]")
    #gruppo2 = df.groupby('Failure Type').agg({"Air temperature [K]":"median", "Process temperature [K]":"median"})
    #st.write(gruppo2)
	
		campi_dataset = load_column_data() # ritorna i nomi dei campi
	
		drop_down_column = food_dataset["Food_Name"]
		food_type = st.selectbox("Select column:", campi_dataset, key=f"uno")	
		ft = []
		fpw = []
		tpd = []
		quan = []
			
		num_food_items = st.number_input("Enter the number of food items: ", step = 1)
			
			    # Create widgets outside the loop
		food_type_widget = st.empty()
		frequency_per_week_widget = st.empty()
		times_per_day_widget = st.empty()
		quantity_widget = st.empty()
			
		counter = 0
			
		if st.session_state["num_entered"] < num_food_items:
			food_type = food_type_widget.selectbox("Select the type of food:", drop_down_column, key=f"food_type_input_{len(ft)}")
			frequency_per_week = frequency_per_week_widget.number_input("Enter the frequency per week for food:", key=f"frequency_per_week_input_{len(fpw)}", step=1)
			times_per_day      = times_per_day_widget.number_input("Enter how many times per day for food:", key=f"times_per_day_input_{len(tpd)}", step=1)
			quantity           = quantity_widget.number_input("Enter the quantity in grams for food:", key=f"quantity_input_{len(quan)}", step=1)
		
			if st.button("Submit"):
		            st.session_state.food_items.append({
		                'food_type': food_type,
		                'frequency_per_week': frequency_per_week,
		                'times_per_day': times_per_day,
		                'quantity': quantity
		            })
		
		            ft.append(food_type)
		            fpw.append(frequency_per_week)
		            tpd.append(times_per_day)
		            quan.append(quantity)
		
		            st.session_state["num_entered"] += 1
		
		            st.rerun()
		else:
			st.write("No more food to enter")
		
			st.write("Food items entered")
			st.write(st.session_state.food_items)

#calorie_counter()
if 'dati' not in st.session_state:
	pass
else:
	field_counter()
