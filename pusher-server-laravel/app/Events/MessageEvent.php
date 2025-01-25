<?php

namespace App\Events;

use Illuminate\Broadcasting\Channel;
use Illuminate\Contracts\Broadcasting\ShouldBroadcast;

class MessageEvent implements ShouldBroadcast
{
    public $message;
    public $sender;

    public function __construct($message, $sender = 'laravel')
    {
        $this->message = $message;
        $this->sender = $sender;
    }

    public function broadcastOn()
    {
        return new Channel('python-laravel');
    }

    public function broadcastAs()
    {
        return 'MessageEvent';
    }

    public function broadcastWith()
    {
        return [
            'message' => $this->message,
            'sender' => $this->sender
        ];
    }
}
