import streamlit as st

def login():
    """Handles the user login process."""
    st.session_state.logged_in = st.session_state.get('logged_in', False)
    st.title('User Login')
    if not st.session_state.logged_in:
        username = st.text_input('Enter the Username:')
        password = st.text_input('Enter the password:', type='password')
        email=st.text_input('Enter the emailID:')
        
        if st.button('Login'):
            if username == 'user' and password == 'password':
                st.session_state.logged_in = True
                st.success('Logged in successfully!')
            else:
                st.error('Invalid username or password')
    else:
        st.success('Welcome back, user!')
        if st.button('Logout'):
            st.session_state.logged_in = False
            st.experimental_rerun()

def main():
    """Main application function."""
    st.title('User Login')
    login()

if __name__ == '__main__':
    main()
