import sys

if __name__ == "__main__":
    print("WARNING! This will DROP any existing tables and rebuild the schema.")

    i = 0
    while i < 3:
        print("Proceed (yes/no)?: ", end='')
        answer = input()
        if answer == 'yes':
            try:
                from models import *
                from sqlalchemy import create_engine
                from config import DB_URI

                engine = create_engine(DB_URI)
                print("Type 'yes' again to confirm: ", end='')
                confirmation = input()
                if confirmation == 'yes':
                    Base.metadata.drop_all(engine)
                    Base.metadata.create_all(engine)
                    print("New DB schema was written.")
                else:
                    print("Abort")
                    sys.exit()
                break
            except Exception as e:
                print(str(e.__class__.__name__) + ': ' + str(e))
                sys.exit()
        elif answer in ('n', 'no', 'exit', 'quit', 'q'):
            break
        else:
            i += 1
            print("Didn't get '%s'." % answer, end=' ')

    print('Bye!')
