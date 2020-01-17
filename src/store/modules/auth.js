const state = {
    token: null,
    user: null,
    userType: null,
    error: null
};

const mutations = {
    SET_TOKEN(state, token) {
        state.token = token;
    },
    SET_USER(state, user) {
        state.user = user;
    },
    SET_USERTYPE(state, userType) {
        state.userType = userType;
    },
    SET_ERROR(state, error) {
        state.error = error;
    }
};

const actions = {   
    login({ commit }, { userEmail, userPassword, userType }) {
        let requestBody = {
            userEmail,
            userPassword,
            userType
        };
        return fetch('http://127.0.0.1:8000/api/user/login/', {
            method: 'POST',
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify(requestBody)
        }).then(data => {
            return data.json();
        }).then(data => {
            commit('SET_TOKEN', data.token);
            commit('SET_USER', data.user);
            commit('SET_USERTYPE', userType);
        }).catch(err => {
            // eslint-disable-next-line
            console.log(err);
            commit('SET_ERROR', err.message);
        });
    },
    logout({ commit }) {
        commit('SET_TOKEN', null);
        commit('SET_USER', null);
    },
    createClient({ commit, dispatch }, { firstName, lastName, email, birthday, state, city, password }) {
        //NEED TO GET THE INFO HERE
        let bodyRequest = {
            firstName,
            lastName,
            email,
            birthday,
            state,
            city,
            password
        };

        return fetch('http://127.0.0.1:8000/api/user/client/create/', {
            method: 'POST',
            headers: {
                'Content-Type': "application/json"
            },
            body: JSON.stringify(bodyRequest)
        }).then(data => {
            return data.json();
        }).then(data => {
            commit('SET_TOKEN', data.token);
            commit('SET_USER', data.user);
            if(data.first_name) {
                dispatch('login', { userEmail: email, userPassword: password, userType: 'Client' });
            }
        }).catch(err => {
            // eslint-disable-next-line
            console.log(err);
        });
    },
    createBusiness({ commit, dispatch }, { name, email, state, city, password }) {
        let requestBody = {
            name,
            email,
            state,
            city,
            password
        };

        return fetch('http://127.0.0.1:8000/api/user/business/create/', {
            method: 'POST',
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify(requestBody)
        }).then(data => {
            return data.json();
        }).then(data => {
            commit('SET_TOKEN', data.token);
            commit('SET_USER', data.user);
            if(data.name) {
                dispatch('login', { userEmail: email, userPassword: password, userType: 'Business' });
            }
        }).catch(err => {
            // eslint-disable-next-line
            console.log(err);
        });
    },
    changeProfilePhoto({ commit, getters }, { photo }) {
        const formData = new FormData();
        formData.append('photo', photo);

        return fetch('http://127.0.0.1:8000/api/user/photo_uploader/', {
            method: 'PUT',
            headers: {
                'Token': getters.token,
                'User-Type': getters.userType 
            },
            body: formData
        }).then(data => {
            return data.json();
        }).then(data => {
            commit('SET_USER', data)
        }).catch(err => {
            //eslint-disable-next-line
            console.log(err);
        });
    }
};

const getters = {
    token: state => state.token,
    user: state => state.user,
    userType: state => state.userType,
    error: state => state.error
};

const authModule = {
    state,
    mutations,
    actions,
    getters
};

export default authModule;