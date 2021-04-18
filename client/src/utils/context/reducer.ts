import { Action, ActionKind, State } from "../constants";

const Reducer = (state: State, action: Action): State => {
    const { type, payload } = action;

    switch (type) {
        case ActionKind.signIn:
            console.log("sign in reducer")
            return {
                ...state,
                authData: payload
            };
        case ActionKind.signOut:
            console.log("sign out reducer")
            return {
                ...state,
                authData: null
            };
        default:
            return state;
    }
};

export default Reducer;