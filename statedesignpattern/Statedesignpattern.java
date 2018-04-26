package statedesignpattern;

/**
 *
 * @author jrmathson
 * 
 * This design pattern changes a bosses mood based on if employees call out.
 */


interface BossesState {
    void writeMood(StateContext context, String shiftrequests);
}

// Boss is happy
class StateHappy implements BossesState {
    @Override
    public void writeMood(final StateContext context, final String shiftrequests) {
        int callins = context.requests(shiftrequests);
        if(callins > 0) {
            System.out.println(Statedesignpattern.ANSI_BLUE + "Manager is Concerned"
                     + " because " + callins + " employee has called out"  + Statedesignpattern.ANSI_RESET);
            context.setState(new StateStressed());
        }
        else
            System.out.println(Statedesignpattern.ANSI_GREEN + "Manager is Happy because "
                    + "all shifts are covered" + Statedesignpattern.ANSI_RESET);
    }
}

// Boss is stressed
class StateStressed implements BossesState {
    @Override
    public void writeMood(final StateContext context, final String shiftrequests) {
        int callins = context.requests(shiftrequests);
        if (callins == 2) {
            System.out.println(Statedesignpattern.ANSI_YELLOW + "Manager is Getting Irritated"
                            + " because " + callins + " employees have called out!" + Statedesignpattern.ANSI_RESET);
        }
        
        if (callins == 1) {
            System.out.println(Statedesignpattern.ANSI_BLUE + "Manager is Feeling Better"
                            + " because only " + callins + " shift needs covered now!" + Statedesignpattern.ANSI_RESET);
        }
        
        if (callins > 2) {
            context.setState(new StatePissed());
            System.out.println(Statedesignpattern.ANSI_RED + "Manager is Full on Pissed "
                + " because " + callins + " employees have called out!" + Statedesignpattern.ANSI_RESET);
            
        }
        if (callins < 1) {
            context.setState(new StateHappy());
            System.out.println(Statedesignpattern.ANSI_GREEN + "Manager is Happy because "
                    + "all shifts are covered" + Statedesignpattern.ANSI_RESET);
        }
    }
}

// Boss is pissed
class StatePissed implements BossesState {
    @Override
    public void writeMood(final StateContext context, final String shiftrequests) {
        int callins = context.requests(shiftrequests);
        if(callins < 3) {
            context.setState(new StateStressed());
            System.out.println(Statedesignpattern.ANSI_YELLOW + "Manager has Cooled Down"
                            + " because only " + callins + " shifts need covered!" + Statedesignpattern.ANSI_RESET);
        }
        else {
            System.out.println(Statedesignpattern.ANSI_RED + "Manager is Full on Pissed "
                    + "because " + callins + " employees have called out" + Statedesignpattern.ANSI_RESET);
        }
    }
}

class StateContext {
    private BossesState myState;
    public int numrequests;
    
    StateContext() {
        setState(new StateHappy());
    }
    
    void setState(final BossesState newState) {
        myState = newState;
    }

    public void writeMood(final String shiftrequests) {
        myState.writeMood(this, shiftrequests);
    }
    
    public int requests(String request) {
        if (request == "Can't Work") {
            numrequests++;
        }
        else if (request == "Can Work") {
            numrequests--;
            if (numrequests < 0) {
                numrequests = 0;
            }
        }
        else
            numrequests = 0;
        return numrequests;
    }
   
}

public class Statedesignpattern {
    public static final String ANSI_RED = "\u001B[31m";
    public static final String ANSI_GREEN = "\u001B[32m";
    public static final String ANSI_YELLOW = "\u001B[33m";
    public static final String ANSI_BLUE = "\u001B[34m";
    public static final String ANSI_RESET = "\u001B[0m";
    public static void main(String[] args) {
        final StateContext sc = new StateContext();

        /* 
        *   Type in either "Can Work" or "Can't Work" to change the state 
        *   of the bosses mood!
        
        * - His initial mood is happy
        
        * - Green is Happy
        * - Blue is Concerned
        * - Yellow is almost Pissed
        * - Red is Full on Pissed
        */
        
        sc.writeMood("No Changes");
        sc.writeMood("Can't Work");
        sc.writeMood("Can Work"); 
        sc.writeMood("Can't Work");
        sc.writeMood("Can't Work");
        sc.writeMood("Can't Work");
        sc.writeMood("Can't Work");
        sc.writeMood("Can Work");
        sc.writeMood("Can Work");
        sc.writeMood("Can Work");
        sc.writeMood("Can Work");
    }
}

