# KanisaOS
Kanisa is a swahili word meaning church by adding the os it would translate to church operating system, it's purpose is to help spiritual leaders to make notes about participants such as when
parisioners were baptised, communicant/not, confirmed/not, married/not various departments like mother's union and men's association and the community paristioners belong.

**Brief history** of how the project came to be. My local church got a new reverend and his first assignment was to register all members of the church afresh because the records that he currently 
had did not reflect the number of members. He also wanted a system where the records would be stored as a soft copy, the available software is EasyWorship for keeping church records downside of 
it its not possible to customise it to suit your own needs. I volunteered to create the system and thats how KanisaOS was born.

### Design
The requirements were straight forward security of the system, ability to update records and destroy records. The system needs to adapt to the needs of the church membership form finally 
the records should be available and accessible anywhere anytime.

## Software Features
1. **User management**
   Users are able to login, logout, signup and reset password using their gmail accounts. All of this is done using the allauth package.
2. **Create Records**
   Use forms to create new records for members
3. **Update**
   Already exisiting record can be edited with new information.
4. **Delete**
   An existing record can be removed or destroyed.
5.**Get records**
   All records are displayed in a table format.

 ## Stack

 ### Server side
Django framework

### Client side
TailwindCSS
HTML
CSS

## Database
**Production** - Postgres
**Development** - SQLite

