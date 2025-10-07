<?php

class Lasagna
{
    public function expectedCookTime():int
    {
        // Implement the expectedCookTime method
        return 40;

    }

    public function remainingCookTime(int $elapsed_minutes): int  
    {
        // Implement the remainingCookTime method
        return $this->expectedCookTime() - $elapsed_minutes;
    }

    public function totalPreparationTime(int $layers_to_prep): int
    {
        // Implement the totalPreparationTime method
        return $layers_to_prep*2;
    }

    public function totalElapsedTime(int $layers_to_prep, int $elapsed_minutes): int
    {
        // Implement the totalElapsedTime method
        return $this->totalPreparationTime($layers_to_prep) + $elapsed_minutes;
    }

    public function alarm():string
    {
        // Implement the alarm method
        return 'Ding!';
    }
}
