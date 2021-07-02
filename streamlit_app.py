# Sidebar Column
st.sidebar.title('Sidebar Widgets')
#radio button 
rating = st.sidebar.radio('Are You Happy with the Example',('Yes','No','Not Sure'))
if rating == 'Yes':
    st.sidebar.success('Thank You for Selecting Yes')
elif rating =='No':
    st.sidebar.info('Thank You for Selecting No')
elif rating =='Not Sure':
    st.sidebar.info('Thank You for Selecting Not sure')
#selectbox
rating = st.sidebar.selectbox("How much would you rate this App? ",
                     ['5 Stars', '4 Stars', '3 Stars','2 Stars','1 Star'])
st.sidebar.success(rating)
st.sidebar.write('Find Square of a Number')
#slider
get_number = st.sidebar.slider("Select a Number", 1, 10)
st.sidebar.write('Square of Number',get_number, 'is', get_number*get_number)
