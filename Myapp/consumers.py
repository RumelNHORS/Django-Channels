from channels.consumer import SyncConsumer, AsyncConsumer


#SyncConsumer here
class MySyncConsumer(SyncConsumer):
    
    #This handeler is called when client initially opens a connection and is about to finish the webSocket handshake
    def websocket_connect(self, event):
        print('Websocket Connected...')
    
    #This handeler is called when data recived from client  
    def websocket_recive(self, event):
        print('Websocket Recived...')
    
    #This handelers is called when either connection to the client is lost, either from the client closing the connection, the server closing the connection, or loss of the socket   
    def websocket_disconnect(self, event):
        print('Websocket Disconnected...')
        
        
#AsyncConsumer here
class MyAsyncConsumer(AsyncConsumer):
    
    #This handeler is called when client initially opens a connection and is about to finish the webSocket handshake
    async def websocket_connect(self, event):
        print('Websocket Connected...')
    
    #This handeler is called when data recived from client  
    async def websocket_recive(self, event):
        print('Websocket Recived...')
    
    #This handelers is called when either connection to the client is lost, either from the client closing the connection, the server closing the connection, or loss of the socket   
    async def websocket_disconnect(self, event):
        print('Websocket Disconnected...')