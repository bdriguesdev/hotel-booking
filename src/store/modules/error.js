const state = {
    errorMsg: null
};

const mutations = {
    SET_ERROR(state, value) {
        state.errorMsg = value;
    }
};

const actions = {
    changeError({ commit }, value) {
        commit('SET_ERROR', value);
    }
}

const getters = {
    errorMsg: state => state.errorMsg
}

const errorModule = {
    state,
    mutations,
    actions,
    getters
};

export default errorModule;